from feature.repository.car.car_repository import CarRepository
from feature.domain.model.car import Car

class CarUseCase:
    def __init__(self, car_repository: CarRepository):
        self.car_repository = car_repository

    def get_cars(self):
        return self.car_repository.get_cars()

    def save_car(self, car: Car):
        self.car_repository.save_car(car)

    def delete_car(self, car_id):
        self.car_repository.delete_car(car_id)

    def find_by_plate(self, plate):
        return self.car_repository.find_by_plate(plate)

    def car_hable_to_rent(self, plate, disponibility):
        return self.car_repository.car_hable_to_rent(plate, disponibility)