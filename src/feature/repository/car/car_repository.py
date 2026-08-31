from abc import ABC, abstractmethod

class CarRepository(ABC):
    
    @abstractmethod
    def get_cars(self):
        pass

    @abstractmethod
    def save_car(self, car):
        pass

    @abstractmethod
    def delete_car(self, car_id):
        pass

    @abstractmethod
    def find_by_plate(self, plate):
            pass

    @abstractmethod
    def car_hable_to_rent(self, plate, disponibility):
            pass