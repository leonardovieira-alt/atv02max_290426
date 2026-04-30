from service.usuario_service import UsuarioService
from controller.usuario_controller import UsuarioController
from view.usuario_view import UsuarioView

def main():
    # Inicialização das camadas
    service = UsuarioService()
    view = UsuarioView()
    controller = UsuarioController(service, view)

    while True:
        opcao = view.mostrar_menu()

        if opcao == "1":
            controller.request_cadastro()
        elif opcao == "2":
            controller.request_listagem()
        elif opcao == "3":
            controller.request_consulta()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            view.mostrar_mensagem("Opção inválida.")

if __name__ == "__main__":
    main()