from feature.domain.model.rent import Rent
from feature.repository.rent.rent_repository import RentRepository
from feature.repository.car.car_repository import CarRepository
from feature.repository.client.client_repository import ClientRepository

class RentUseCase:
    def __init__(self, rent_repository: RentRepository, car_repository: CarRepository, client_repository: ClientRepository):
        self.rent_repository = rent_repository
        self.car_repository = car_repository
        self.client_repository = client_repository

    def get_rents(self):
        return self.rent_repository.get_rents()

    def save_rent(self, rent: Rent):
        if not self.car_repository.car_hable_to_rent(rent.car_plate, True):
            raise Exception("Car is not available for rent.")
        if not self.client_repository.find_by_cpf(rent.client_cpf):
            raise Exception("Client does not exist.")
        self.rent_repository.save_rent(rent)
        # Update car availability
        car = self.car_repository.find_by_plate(rent.car_plate)
        car.disponibility = False
        self.car_repository.save_car(car)

    def delete_rent(self, rent_id):
        rent = self.rent_repository.find_by_id(rent_id)
        if rent:
            # Update car availability
            car = self.car_repository.find_by_plate(rent.car_plate)
            car.disponibility = True
            self.car_repository.save_car(car)
            self.rent_repository.delete_rent(rent_id)

    def find_by_id(self, rent_id):
        return self.rent_repository.find_by_id(rent_id)