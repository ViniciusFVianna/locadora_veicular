import unittest


class ImportSmokeTest(unittest.TestCase):
    def test_project_modules_import(self):
        from feature.datasource.json_datasource import JsonDataSource
        from feature.datasource.json_datasource_impl import JsonDataSourceImpl
        from feature.domain.model.car import Car
        from feature.domain.model.client import Client
        from feature.domain.model.rent import Rent
        from feature.repository.car.car_repository_impl import CarRepositoryImpl
        from feature.repository.client.client_repository_impl import ClientRepositoryImpl
        from feature.repository.rent.rent_repository_impl import RentRepositoryImpl

        self.assertTrue(callable(JsonDataSource.get_data))
        self.assertTrue(callable(JsonDataSourceImpl.get_data))
        self.assertTrue(issubclass(CarRepositoryImpl, object))
        self.assertTrue(issubclass(ClientRepositoryImpl, object))
        self.assertTrue(issubclass(RentRepositoryImpl, object))
        self.assertEqual(Car.__name__, 'Car')
        self.assertEqual(Client.__name__, 'Client')
        self.assertEqual(Rent.__name__, 'Rent')


if __name__ == '__main__':
    unittest.main()
