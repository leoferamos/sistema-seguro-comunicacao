import pwinput
import auth
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        limpar_tela()
        print("\n1. Registrar novo usuário")
        print("2. Fazer login")
        print("3. Listar usuários")
        
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            username = input("Digite um nome de usuário: ")
            password = pwinput.pwinput("Digite uma senha: ")
            print(auth.register_user(username, password))
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            limpar_tela()
            username = input("Digite seu nome de usuário: ")
            password = pwinput.pwinput("Digite sua senha: ")
            token = input("Digite o código TOTP do seu aplicativo autenticador: ")
            print(auth.verificar_login(username, password, token))
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            limpar_tela()
            usuarios = auth.listar_usuarios()
            if usuarios:
                print("\nUsuários cadastrados:")
                for user in usuarios:
                    print(f"ID: {user[0]}, Username: {user[1]}")
            else:
                print("Nenhum usuário cadastrado.")
            input("\nPressione Enter para continuar...")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    menu()
