import sqlite3
import bcrypt
import os
import time

# Define o caminho do banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'users.db')

# Configurações de segurança
MAX_TENTATIVAS = 5  # Número máximo de tentativas de login
BLOQUEIO_TEMPO = 300  # Tempo de bloqueio em segundos (5 minutos)

def inicializar_banco():
    """Cria a tabela de usuários, se não existir."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash BLOB NOT NULL,
            tentativas_falhas INTEGER DEFAULT 0,
            ultimo_login_falho REAL
        )
    ''')
    conn.commit()
    conn.close()

def registrar_usuario(username, password):
    """Registra um novo usuário com senha hasheada."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Verifica se o usuário já existe
    cursor.execute("SELECT * FROM usuarios WHERE username = ?", (username,))
    if cursor.fetchone():
        print("Erro: Nome de usuário já existe.")
        conn.close()
        return False

    # Gera um SALT e hasheia a senha
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode(), salt)

    # Insere o usuário no banco
    cursor.execute(
        "INSERT INTO usuarios (username, password_hash) VALUES (?, ?)",
        (username, password_hash)
    )
    conn.commit()
    conn.close()
    print("Usuário registrado com sucesso!")
    return True

def verificar_login(username, password):
    """Verifica as credenciais do usuário e implementa bloqueio após múltiplas tentativas falhas."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Busca o usuário no banco de dados
    cursor.execute("SELECT id, password_hash, tentativas_falhas, ultimo_login_falho FROM usuarios WHERE username = ?", (username,))
    resultado = cursor.fetchone()

    if resultado:
        user_id, password_hash, tentativas_falhas, ultimo_login_falho = resultado

        # Verifica se o usuário está bloqueado
        if tentativas_falhas >= MAX_TENTATIVAS:
            tempo_restante = BLOQUEIO_TEMPO - (time.time() - ultimo_login_falho)
            if tempo_restante > 0:
                print(f"Conta bloqueada. Tente novamente em {int(tempo_restante)} segundos.")
                conn.close()
                return False
            else:
                # Reseta as tentativas falhas após o período de bloqueio
                cursor.execute("UPDATE usuarios SET tentativas_falhas = 0 WHERE id = ?", (user_id,))
                conn.commit()

        # Verifica a senha
        if bcrypt.checkpw(password.encode(), password_hash):
            print("Login bem-sucedido!")
            # Reseta as tentativas falhas após login bem-sucedido
            cursor.execute("UPDATE usuarios SET tentativas_falhas = 0 WHERE id = ?", (user_id,))
            conn.commit()
            conn.close()
            return True
        else:
            # Incrementa o contador de tentativas falhas
            tentativas_falhas += 1
            cursor.execute(
                "UPDATE usuarios SET tentativas_falhas = ?, ultimo_login_falho = ? WHERE id = ?",
                (tentativas_falhas, time.time(), user_id)
            )
            conn.commit()
            print("Senha incorreta.")
    else:
        print("Usuário não encontrado.")

    conn.close()
    return False

def listar_usuarios():
    """Lista todos os usuários cadastrados (sem exibir senhas)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()

    if usuarios:
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Username: {usuario[1]}")
    else:
        print("Nenhum usuário cadastrado.")

# Inicializa o banco de dados ao executar o script
if __name__ == '__main__':
    inicializar_banco()
    while True:
        print("\n1. Registrar novo usuário")
        print("2. Fazer login")
        print("3. Listar usuários")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            username = input("Digite um nome de usuário: ")
            password = input("Digite uma senha: ")
            registrar_usuario(username, password)
        elif escolha == '2':
            username = input("Digite seu nome de usuário: ")
            password = input("Digite sua senha: ")
            verificar_login(username, password)
        elif escolha == '3':
            listar_usuarios()
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")
