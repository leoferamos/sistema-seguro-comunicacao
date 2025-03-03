import pwinput
import auth
import os
from getch import getch

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    limpar_tela()
    username = input("Digite seu nome de usuário: ")
    while True:
        limpar_tela()
        print(f"Digite seu nome de usuário: {username}")
        password = pwinput.pwinput("Digite sua senha: ")
        resultado = auth.verificar_login(username, password)
        if "Login bem-sucedido" in resultado:
            print(resultado)
            input("\nPressione Enter para continuar...")
            break
        else:
            print(resultado)
            if "Muitas tentativas falharam" in resultado:
                input("\nPressione Enter para continuar...")
                break
            print("\nPressione 'Enter' para tentar novamente ou 'Esc' para voltar ao menu inicial...")
            opcao = getch()
            if opcao == '\x1b':  # Código ASCII para a tecla Esc
                return

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
            confirm_password = pwinput.pwinput("Confirme sua senha: ")
            if password != confirm_password:
                print("Erro: As senhas não coincidem.")
            else:
                print(auth.register_user(username, password))
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            login()

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
