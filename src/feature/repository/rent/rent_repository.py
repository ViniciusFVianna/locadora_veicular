from abc import ABC, abstractmethod

class RentRepository(ABC):
    
    @abstractmethod
    def get_rents(self):
        pass

    @abstractmethod
    def save_rent(self, rent):
        pass

    @abstractmethod
    def delete_rent(self, rent_id):
        pass

    @abstractmethod
    def find_by_plate(self, plate):
            pass

    @abstractmethod
    def find_by_cpf(self, cpf):
            pass