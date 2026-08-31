from feature.datasource.json_datasource import JsonDataSource
from feature.domain.model.client import Client
from feature.repository.client.client_repository import ClientRepository

class ClientRepositoryImpl(ClientRepository):
    def __init__(self, data_source: JsonDataSource):
        self.data_source = data_source

    def get_clients(self):
        data = self.data_source.get_data()
        return [Client(**client) for client in data]

    def save_client(self, client: Client):
        clients = self.get_clients()
        clients.append(client)
        self.data_source.save_data([client.__dict__ for client in clients])

    def delete_client(self, client_id):
        clients = self.get_clients()
        clients = [client for client in clients if client.id != client_id]
        self.data_source.save_data([client.__dict__ for client in clients])

    def find_by_cpf(self, cpf):
        clients = self.get_clients()
        for client in clients:
            if client.cpf == cpf:
                return client
        return None