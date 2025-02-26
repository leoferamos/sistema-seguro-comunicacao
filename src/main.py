from database import init_db
from auth import register_user, verify_user
def main():
   # Inicializa o banco de dados na primeira execução
   init_db()
   while True:
       print("\nSelecione uma opção:")
       print("1 - Registrar usuário")
       print("2 - Login")
       print("3 - Sair")
       option = input("Opção: ")
       if option == "1":
           username = input("Digite o username: ")
           password = input("Digite a senha: ")
           register_user(username, password)
       elif option == "2":
           username = input("Digite o username: ")
           password = input("Digite a senha: ")
           if verify_user(username, password):
               print("Login bem sucedido!")
           else:
               print("Credenciais inválidas.")
       elif option == "3":
           print("Saindo...")
           break
       else:
           print("Opção inválida. Tente novamente.")
if __name__ == '__main__':
   main()