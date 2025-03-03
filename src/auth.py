import sqlite3
import bcrypt
import os
import jwt
import pyotp
import qrcode
import pwinput
from datetime import datetime, timedelta
from logger_config import configure_logger

# Configura o logger
logger = configure_logger()

# Define o caminho do banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'users.db')

# Chave secreta para assinatura JWT
SECRET_KEY = 'your_secret_key'
if not SECRET_KEY:
    raise ValueError("SECRET_KEY não pode estar vazia")

# Dicionário para armazenar tentativas de login e tempos de bloqueio
login_attempts = {}
lockout_time = 5 * 60  # Tempo de bloqueio em segundos (5 minutos)

# Gera um segredo TOTP para o usuário
def generate_totp_secret():
    return pyotp.random_base32()

# Gera um código QR para o segredo TOTP
def get_totp_uri(username, secret):
    totp = pyotp.TOTP(secret)
    return totp.provisioning_uri(name=username, issuer_name="SistemaSeguro")

# Gera e exibe o código QR no terminal
def generate_qr_code(uri):
    qr = qrcode.QRCode()
    qr.add_data(uri)
    qr.make(fit=True)
    qr.print_ascii()

# Verifica o código TOTP
def verify_totp(token, secret):
    totp = pyotp.TOTP(secret)
    return totp.verify(token)

# Registra um novo usuário no banco de dados.
def register_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Normaliza o nome de usuário para minúsculas
    username = username.lower()

    # Verifica se o usuário já existe
    cursor.execute("SELECT * FROM usuarios WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return "Erro: Nome de usuário já existe."

    # Solicita a senha do usuário
    password = pwinput.pwinput("Digite sua senha: ")

    # Gera um SALT e hasheia a senha
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode(), salt)

    # Gera um segredo TOTP
    totp_secret = generate_totp_secret()

    # Insere o novo usuário no banco de dados
    cursor.execute("INSERT INTO usuarios (username, password_hash, totp_secret) VALUES (?, ?, ?)", (username, password_hash, totp_secret))
    conn.commit()
    conn.close()

    # Retorna o URI do TOTP para ser exibido como código QR
    totp_uri = get_totp_uri(username, totp_secret)
    generate_qr_code(totp_uri)
    return f"Usuário registrado com sucesso! Escaneie o código QR no Microsoft Authenticator."

# Gera um token JWT para o usuário.
def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

# Verifica a validade do token JWT.
def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return "Token expirado. Faça login novamente."
    except jwt.InvalidTokenError:
        return "Token inválido. Faça login novamente."

# Verifica se o login do usuário é válido.
def verificar_login(username, password, token):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Normaliza o nome de usuário para minúsculas
    username = username.lower()

    # Solicita a senha do usuário
    password = pwinput.pwinput("Digite sua senha: ")

    # Verifica se o usuário excedeu o limite de tentativas
    if username in login_attempts:
        attempts, last_attempt_time = login_attempts[username]
        if attempts >= 5:
            if (datetime.now() - last_attempt_time).total_seconds() < lockout_time:
                logger.warning(f"Muitas tentativas falharam para o usuário: {username}")
                return "❌ Muitas tentativas falharam. Tente novamente mais tarde."
            else:
                login_attempts[username] = (0, datetime.now())  # Reseta as tentativas após o tempo de bloqueio

    # Busca as credenciais do usuário no banco de dados
    cursor.execute("SELECT id, password_hash, totp_secret FROM usuarios WHERE username = ?", (username,))
    user = cursor.fetchone()

    conn.close()

    # Verifica se o usuário existe e se a senha está correta
    if user and bcrypt.checkpw(password.encode(), user[1]):
        if verify_totp(token, user[2]):
            jwt_token = generate_token(user[0])
            login_attempts[username] = (0, datetime.now())  # Reseta as tentativas após login bem-sucedido
            logger.info(f"Login bem-sucedido para o usuário: {username}")
            return f"✅ Login bem-sucedido! Seu token: {jwt_token}"
        else:
            logger.warning(f"Código TOTP inválido para o usuário: {username}")
            return "❌ Código TOTP inválido."
    else:
        if username in login_attempts:
            attempts, _ = login_attempts[username]
            login_attempts[username] = (attempts + 1, datetime.now())
        else:
            login_attempts[username] = (1, datetime.now())
        logger.warning(f"Login falhou para o usuário: {username}. Tentativas restantes: {5 - login_attempts[username][0]}")
        return f"❌ Login falhou! Verifique suas credenciais. Tentativas restantes: {5 - login_attempts[username][0]}"

# Lista todos os usuários cadastrados no banco de dados.
def listar_usuarios():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, username FROM usuarios ORDER BY id")  
    users = cursor.fetchall()
    conn.close()

    return users
