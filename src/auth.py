import sqlite3
import bcrypt
import os
# Define o caminho do banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'users.db')
def register_user(username, password):
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
   cursor.execute("INSERT INTO usuarios (username, password_hash) VALUES (?, ?)", (username, password_hash))
   conn.commit()
   conn.close()
   print("Usuário registrado com sucesso!")
   return True
# Teste rápido (remova isso depois ou transforme em um input)
if __name__ == '__main__':
   username = input("Digite um nome de usuário: ")
   password = input("Digite uma senha: ")
   register_user(username, password)
   
   def list_users():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("SELECT id, username FROM usuarios")  # Não exibir as senhas

    users = cursor.fetchall()

    conn.close()

    if users:

        print("Usuários cadastrados:")

        for user in users:

            print(f"ID: {user[0]}, Username: {user[1]}")

    else:

        print("Nenhum usuário cadastrado.")
