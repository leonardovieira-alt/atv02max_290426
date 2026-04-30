class UsuarioView:
    def mostrar_menu(self):
        print("\n--- SISTEMA DE USUÁRIOS ---")
        print("1. Cadastrar Usuário")
        print("2. Listar Todos")
        print("3. Buscar por ID")
        print("0. Sair")
        return input("Escolha uma opção: ")

    def obter_dados_usuario(self):
        nome = input("Nome: ")
        email = input("Email: ")
        return nome, email

    def obter_id_consulta(self):
        return int(input("Digite o ID do usuário: "))

    def mostrar_usuarios(self, usuarios):
        print("\n=== LISTA DE USUÁRIOS ===")
        for u in usuarios:
            print(f"ID: {u.id} | Nome: {u.nome} | Email: {u.email}")

    def mostrar_detalhes_usuario(self, u):
        print(f"\n[Resultado] ID: {u.id}, Nome: {u.nome}, Email: {u.email}")

    def mostrar_mensagem(self, msg):
        print(f"\n> {msg}")