import sqlite3
import bcrypt
import os
import jwt
from datetime import datetime, timedelta

# Define o caminho do banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'users.db')

# Certifique-se de definir uma chave secreta forte
SECRET_KEY = 'your_secret_key'
if not SECRET_KEY:
    raise ValueError("SECRET_KEY não pode estar vazia")

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

    # Gera um SALT e hasheia a senha
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode(), salt)

    # Insere o novo usuário no banco de dados
    cursor.execute("INSERT INTO usuarios (username, password_hash) VALUES (?, ?)", (username, password_hash))
    conn.commit()
    conn.close()
    return "Usuário registrado com sucesso!"

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
def verificar_login(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Busca as credenciais do usuário no banco de dados
    cursor.execute("SELECT id, password_hash FROM usuarios WHERE username = ?", (username,))
    user = cursor.fetchone()

    conn.close()

    # Verifica se o usuário existe e se a senha está correta
    if user and bcrypt.checkpw(password.encode(), user[1]):
        token = generate_token(user[0])
        return f"✅ Login bem-sucedido! Seu token: {token}"
    else:
        return "❌ Login falhou! Verifique suas credenciais."

# Lista todos os usuários cadastrados no banco de dados.
def listar_usuarios():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, username FROM usuarios")  
    users = cursor.fetchall()
    conn.close()

    return users
