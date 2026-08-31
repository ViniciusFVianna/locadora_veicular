import os
import sys

SRC_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SRC_ROOT)
for path in (SRC_ROOT, PROJECT_ROOT):
    if path not in sys.path:
        sys.path.insert(0, path)

try:
    from feature.datasource.json_datasource_impl import JsonDataSourceImpl
    from feature.domain.model.car import Car
    from feature.domain.model.client import Client
    from feature.domain.model.rent import Rent
    from feature.repository.car.car_repository_impl import CarRepositoryImpl
    from feature.repository.client.client_repository_impl import ClientRepositoryImpl
    from feature.repository.rent.rent_repository_impl import RentRepositoryImpl
    from feature.usecase.car.car_usecase import CarUseCase
    from feature.usecase.client.clent_usecase import ClientUseCase
    from feature.usecase.rent.rent_usecase import RentUseCase
except ModuleNotFoundError:
    from src.feature.datasource.json_datasource_impl import JsonDataSourceImpl
    from src.feature.domain.model.car import Car
    from src.feature.domain.model.client import Client
    from src.feature.domain.model.rent import Rent
    from src.feature.repository.car.car_repository_impl import CarRepositoryImpl
    from src.feature.repository.client.client_repository_impl import ClientRepositoryImpl
    from src.feature.repository.rent.rent_repository_impl import RentRepositoryImpl
    from src.feature.usecase.car.car_usecase import CarUseCase
    from src.feature.usecase.client.clent_usecase import ClientUseCase
    from src.feature.usecase.rent.rent_usecase import RentUseCase

def menu():
    print("\n==============================")
    print("      LOCADORA DE CARROS      ")
    print("==============================")
    print("1. Cadastrar Carro")
    print("2. Listar Carros")
    print("3. Cadastrar Cliente")
    print("4. Listar Clientes")
    print("5. Realizar Locação (Alugar)")
    print("6. Realizar Devolução")
    print("7. Listar Locações")
    print("0. Sair")

    option = input("\nEscolha uma opção: ")

    if option == "1":
        plate = input("Digite a placa do carro: ")
        model = input("Digite o modelo do carro: ")
        disponibility = True  # Carro disponível por padrão
        car = Car(plate=plate, model=model, disponibility=disponibility)
        car_use_case.save_car(car)
        print("Carro cadastrado com sucesso!")

    elif option == "2":
        cars = car_use_case.get_cars()
        if not cars:
            print("Nenhum carro cadastrado.")
        else:
            print("\nLista de Carros:")
            for car in cars:
                status = "Disponível" if car.disponibility else "Indisponível"
                print(f"Placa: {car.plate}, Modelo: {car.model}, Status: {status}")

    elif option == "3":
        cpf = input("Digite o CPF do cliente: ")
        name = input("Digite o nome do cliente: ")
        client = Client(cpf=cpf, name=name)
        client_use_case.save_client(client)
        print("Cliente cadastrado com sucesso!")

    elif option == "4":
        clients = client_use_case.get_clients()
        if not clients:
            print("Nenhum cliente cadastrado.")
        else:
            print("\nLista de Clientes:")
            for client in clients:
                print(f"CPF: {client.cpf}, Nome: {client.name}")

    elif option == "5":
        car_plate = input("Digite a placa do carro que deseja alugar: ")
        client_cpf = input("Digite o CPF do cliente: ")
        rent = Rent(car_plate=car_plate, client_cpf=client_cpf)
        try:
            rent_use_case.save_rent(rent)
            print("Locação realizada com sucesso!")
        except Exception as e:
            print(f"Erro ao realizar locação: {e}")

    elif option == "6":
        rent_id = input("Digite o ID da locação que deseja devolver: ")
        try:
            rent_use_case.delete_rent(rent_id)
            print("Devolução realizada com sucesso!")
        except Exception as e:
            print(f"Erro ao realizar devolução: {e}")

    elif option == "7":
            rents = rent_use_case.get_rents()
            if not rents:
                print("Nenhuma locação registrada.")
            else:
                print("\nLista de Locações:")
                for rent in rents:
                    print(f"ID: {rent.id}, Placa do Carro: {rent.car_plate}, CPF do Cliente: {rent.client_cpf}")

    elif option == "0":
        print("Saindo do sistema...")
        exit()

    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    database_dir = os.path.join(SRC_ROOT, "database")
    os.makedirs(database_dir, exist_ok=True)

    cars_file = os.path.join(database_dir, "cars.json")
    clients_file = os.path.join(database_dir, "clients.json")
    rents_file = os.path.join(database_dir, "rents.json")

    car_use_case = CarUseCase(car_repository=CarRepositoryImpl(data_source=JsonDataSourceImpl(cars_file)))
    client_use_case = ClientUseCase(client_repository=ClientRepositoryImpl(data_source=JsonDataSourceImpl(clients_file)))
    rent_use_case = RentUseCase(rent_repository=RentRepositoryImpl(data_source=JsonDataSourceImpl(rents_file)),
                                 car_repository=car_use_case.car_repository,
                                 client_repository=client_use_case.client_repository)

    while True:
        menu()