import sqlite3
import os
# Define o caminho do banco na pasta 'data'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'users.db')
def get_connection():
   return sqlite3.connect(DB_PATH)
def init_db():
   conn = get_connection()
   cursor = conn.cursor()
   # Cria a tabela de usuários; usamos BLOB para armazenar o hash binário
   cursor.execute('''
   CREATE TABLE IF NOT EXISTS usuarios (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       username TEXT UNIQUE NOT NULL,
       password_hash BLOB NOT NULL
   )
   ''')
   conn.commit()
   conn.close()