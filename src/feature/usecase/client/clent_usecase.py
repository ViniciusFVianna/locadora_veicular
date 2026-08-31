from feature.repository.client.client_repository import ClientRepository
from feature.domain.model.client import Client

class ClientUseCase:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def get_clients(self):
        return self.client_repository.get_clients()

    def save_client(self, client: Client):
        self.client_repository.save_client(client)

    def delete_client(self, client_id):
        self.client_repository.delete_client(client_id)

    def find_by_cpf(self, cpf):
        return self.client_repository.find_by_cpf(cpf)
