import sqlite3
import bcrypt
import os

# Define o caminho do banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'users.db')

# Registra um novo usuário no banco de dados.
def register_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

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
        return "✅ Login bem-sucedido!"
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
