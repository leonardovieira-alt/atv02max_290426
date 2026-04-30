from model.usuario import Usuario
from repository.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()

    def criar_usuario(self, nome, email):
        if "@" not in email:
            raise ValueError("Email inválido: deve conter '@'")
        
        novo_usuario = Usuario(nome, email)
        self.repository.salvar(novo_usuario)

    def listar_usuarios(self):
        return self.repository.listar()

    def consultar_usuario(self, usuario_id):
        usuario = self.repository.buscar_por_id(usuario_id)
        if not usuario:
            raise ValueError("Erro: Usuário não encontrado no sistema.")
        return usuario