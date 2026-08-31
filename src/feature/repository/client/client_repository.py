from abc import ABC, abstractmethod

class ClientRepository(ABC):
    
    @abstractmethod
    def get_clients(self):
        pass

    @abstractmethod
    def save_client(self, client):
        pass

    @abstractmethod
    def delete_client(self, client_id):
        pass

    @abstractmethod
    def find_by_cpf(self, cpf):
        pass