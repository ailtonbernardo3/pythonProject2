class PasswordManager:
    def __init__(self):
        self.credentials = {}

    def save_credentials(self, username, password):
        if username in self.credentials:
            return "Login já existe. Por favor, escolha outro nome de usuário."
        for stored_username, stored_password in self.credentials.items():
            if stored_password == password:
                return "Senha já está sendo usada por outro usuário. Por favor, escolha outra senha."
        self.credentials[username] = password
        return "Credenciais salvas com sucesso!"

    def get_password(self, username):
        if username in self.credentials:
            return self.credentials[username]
        else:
            return "Usuário não encontrado."

def main():
    password_manager = PasswordManager()

    while True:
        print("\n1. Salvar Credenciais")
        print("2. Obter Senha")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            username = input("Digite o nome de usuário: ")
            password = input("Digite a senha: ")
            result = password_manager.save_credentials(username, password)
            print(result)
        elif choice == "2":
            username = input("Digite o nome de usuário para obter a senha: ")
            password = password_manager.get_password(username)
            print("Senha:", password)
        elif choice == "3":
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
