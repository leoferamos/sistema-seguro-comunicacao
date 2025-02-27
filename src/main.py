import auth

def menu():
    while True:
        print("\n1. Registrar novo usuário")
        print("2. Fazer login")
        print("3. Listar usuários")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            username = input("Digite um nome de usuário: ")
            password = input("Digite uma senha: ")
            print(auth.register_user(username, password))

        elif opcao == "2":
            username = input("Digite seu nome de usuário: ")
            password = input("Digite sua senha: ")
            token = input("Digite o código TOTP do seu aplicativo autenticador: ")
            print(auth.verificar_login(username, password, token))

        elif opcao == "3":
            usuarios = auth.listar_usuarios()
            if usuarios:
                print("\nUsuários cadastrados:")
                for user in usuarios:
                    print(f"ID: {user[0]}, Username: {user[1]}")
            else:
                print("Nenhum usuário cadastrado.")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
