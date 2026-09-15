from locadora_veicular.models.cliente import Cliente
from locadora_veicular.models.veiculo import Veiculo
from locadora_veicular.repositories.cliente_repository import ClienteRepository
from locadora_veicular.repositories.veiculo_repository import VeiculoRepository


class LocacaoService:
    def __init__(self, cliente_repository: ClienteRepository, veiculo_repository: VeiculoRepository):
        self.cliente_repository = cliente_repository
        self.veiculo_repository = veiculo_repository

    def cadastrar_cliente(self, cpf: str, nome: str) -> Cliente:
        cliente = Cliente(cpf=cpf, nome=nome)
        return self.cliente_repository.save(cliente)

    def cadastrar_veiculo(self, placa: str, modelo: str) -> Veiculo:
        veiculo = Veiculo(placa=placa, modelo=modelo, disponivel=True)
        return self.veiculo_repository.save(veiculo)

    def alugar_veiculo(self, cpf: str, placa: str) -> None:
        cliente = self.cliente_repository.find_by_cpf(cpf)
        if cliente is None:
            raise ValueError("Cliente não encontrado.")

        veiculo = self.veiculo_repository.find_by_placa(placa)
        if veiculo is None:
            raise ValueError("Veículo não encontrado.")
        if not veiculo.disponivel:
            raise ValueError("Veículo indisponível para locação.")

        veiculo.disponivel = False
        self.veiculo_repository.update(veiculo)
