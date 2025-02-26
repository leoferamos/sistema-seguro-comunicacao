import sqlite3
import os
# Define o caminho do banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')
# Garante que o diretório 'data' exista
os.makedirs(DATA_DIR, exist_ok=True)
DB_PATH = os.path.join(DATA_DIR, 'users.db')
def init_db():
   conn = sqlite3.connect(DB_PATH)
   cursor = conn.cursor()
   cursor.execute('''
   CREATE TABLE IF NOT EXISTS usuarios (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       username TEXT UNIQUE NOT NULL,
       password_hash BLOB NOT NULL
   )
   ''')
   conn.commit()
   conn.close()
   print("Banco de dados criado com sucesso.")
if __name__ == '__main__':
   init_db()