from feature.datasource.json_datasource import JsonDataSource
from feature.domain.model.rent import Rent
from feature.repository.rent.rent_repository import RentRepository

class RentRepositoryImpl(RentRepository):
    def __init__(self, data_source: JsonDataSource):
        self.data_source = data_source

    def get_rents(self):
        data = self.data_source.get_data()
        return [Rent(**rent) for rent in data]

    def save_rent(self, rent: Rent):
        rents = self.get_rents()
        rents.append(rent)
        self.data_source.save_data([rent.__dict__ for rent in rents])

    def delete_rent(self, rent_id):
        rents = self.get_rents()
        rents = [rent for rent in rents if rent.id != rent_id]
        self.data_source.save_data([rent.__dict__ for rent in rents])

    def find_by_plate(self, plate):
        rents = self.get_rents()
        for rent in rents:
            if rent.plate == plate:
                return rent
        return None

    def find_by_cpf(self, cpf):
        rents = self.get_rents()
        for rent in rents:
            if rent.cpf == cpf:
                return rent
        return None