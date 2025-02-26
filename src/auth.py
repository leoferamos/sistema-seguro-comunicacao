import bcrypt
from database import get_connection
def register_user(username: str, password: str):
   # Gera o salt e o hash da senha
   salt = bcrypt.gensalt()
   password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
   conn = get_connection()
   cursor = conn.cursor()
   try:
       cursor.execute(
           'INSERT INTO usuarios (username, password_hash) VALUES (?, ?)',
           (username, password_hash)
       )
       conn.commit()
       print("Usuário registrado com sucesso!")
   except Exception as e:
       print("Erro ao registrar usuário:", e)
   finally:
       conn.close()
def verify_user(username: str, password: str) -> bool:
   conn = get_connection()
   cursor = conn.cursor()
   cursor.execute(
       'SELECT password_hash FROM usuarios WHERE username = ?',
       (username,)
   )
   result = cursor.fetchone()
   conn.close()
   if result:
       stored_hash = result[0]
       # Verifica se a senha fornecida bate com o hash armazenado
       return bcrypt.checkpw(password.encode('utf-8'), stored_hash)
   return False