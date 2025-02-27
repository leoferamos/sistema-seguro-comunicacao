import auth
import os

#Verifica se o sistema operacional é Windows, Linux ou Mac e limpa a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Menu principal
def menu():
    while True:
        clear_screen()
        print("\n1. Registrar novo usuário")
        print("2. Fazer login")
        print("3. Listar usuários")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            clear_screen()
            username = input("Digite um nome de usuário: ")
            password = input("Digite uma senha: ")
            print(auth.register_user(username, password))
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            clear_screen()
            username = input("Digite seu nome de usuário: ")
            password = input("Digite sua senha: ")
            print(auth.verificar_login(username, password))
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            clear_screen()
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
