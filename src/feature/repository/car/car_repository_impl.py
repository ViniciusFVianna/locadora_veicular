from feature.datasource.json_datasource import JsonDataSource
from feature.domain.model.car import Car
from feature.repository.car.car_repository import CarRepository

class CarRepositoryImpl(CarRepository):
    def __init__(self, data_source: JsonDataSource):
        self.data_source = data_source

    def get_cars(self):
        data = self.data_source.get_data()
        return [Car(**car) for car in data]

    def save_car(self, car: Car):
        cars = self.get_cars()
        cars.append(car)
        self.data_source.save_data([car.__dict__ for car in cars])

    def delete_car(self, car_id):
        cars = self.get_cars()
        cars = [car for car in cars if car.id != car_id]
        self.data_source.save_data([car.__dict__ for car in cars])

    def find_by_plate(self, plate):
        cars = self.get_cars()
        for car in cars:
            if car.plate == plate:
                return car
        return None

    def car_hable_to_rent(self, plate, disponibility):
        car = self.find_by_plate(plate)
        if car:
            return car.disponibility == disponibility
        return False