class UsuarioController:
    def __init__(self, service, view):
        self.service = service
        self.view = view

    def request_cadastro(self):
        try:
            nome, email = self.view.obter_dados_usuario()
            self.service.criar_usuario(nome, email)
            self.view.mostrar_mensagem("Usuário cadastrado com sucesso!")
        except Exception as e:
            self.view.mostrar_mensagem(str(e))

    def request_listagem(self):
        usuarios = self.service.listar_usuarios()
        self.view.mostrar_usuarios(usuarios)

    def request_consulta(self):
        try:
            usuario_id = self.view.obter_id_consulta()
            usuario = self.service.consultar_usuario(usuario_id)
            self.view.mostrar_detalhes_usuario(usuario)
        except ValueError as e:
            self.view.mostrar_mensagem(str(e))