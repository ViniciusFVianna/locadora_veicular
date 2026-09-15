import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from locadora_veicular.core.database import init_db
from locadora_veicular.repositories.cliente_repository import ClienteRepository
from locadora_veicular.repositories.veiculo_repository import VeiculoRepository
from locadora_veicular.services.locacao_service import LocacaoService


def menu() -> None:
    while True:
        try:
            print("\n==============================")
            print("      LOCADORA DE VEÍCULOS      ")
            print("==============================")
            print("1. Cadastrar Cliente")
            print("2. Listar Clientes")
            print("3. Cadastrar Veículo")
            print("4. Listar Veículos")
            print("5. Alugar Veículo")
            print("0. Sair")

            option = input("\nEscolha uma opção: ")

            match option:
                case "1":
                    cpf = input("Digite o CPF do cliente: ")
                    nome = input("Digite o nome do cliente: ")
                    service.cadastrar_cliente(cpf, nome)
                    print("Cliente cadastrado com sucesso!")

                case "2":
                    clientes = cliente_repository.list_all()
                    if not clientes:
                        print("Nenhum cliente cadastrado.")
                        continue
                    print("\nClientes:")
                    for cliente in clientes:
                        print(f"CPF: {cliente.cpf} | Nome: {cliente.nome}")

                case "3":
                    placa = input("Digite a placa do veículo: ")
                    modelo = input("Digite o modelo do veículo: ")
                    service.cadastrar_veiculo(placa, modelo)
                    print("Veículo cadastrado com sucesso!")

                case "4":
                    veiculos = veiculo_repository.list_all()
                    if not veiculos:
                        print("Nenhum veículo cadastrado.")
                        continue
                    print("\nVeículos:")
                    for veiculo in veiculos:
                        status = "Disponível" if veiculo.disponivel else "Indisponível"
                        print(f"Placa: {veiculo.placa} | Modelo: {veiculo.modelo} | Status: {status}")

                case "5":
                    cpf = input("Digite o CPF do cliente: ")
                    placa = input("Digite a placa do veículo: ")
                    try:
                        service.alugar_veiculo(cpf, placa)
                        print("Locação realizada com sucesso!")
                    except ValueError as exc:
                        print(f"Erro: {exc}")

                case "0":
                    print("Saindo do sistema...")
                    raise SystemExit

                case _:
                    print("Opção inválida. Tente novamente.")

        except (KeyboardInterrupt, EOFError):
            print("\nInterrupção detectada. Encerrando o sistema...")
            raise SystemExit
        except Exception as exc:
            print(f"Erro inesperado: {exc}")
            continue


if __name__ == "__main__":
    init_db()
    cliente_repository = ClienteRepository()
    veiculo_repository = VeiculoRepository()
    service = LocacaoService(cliente_repository, veiculo_repository)

    try:
        menu()
    except SystemExit:
        pass
