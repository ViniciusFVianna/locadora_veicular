class Rent:
    def __init__(self, car_plate, client_cpf, id=None, car_id=None, client_id=None):
        self.id = id
        self.car_plate = car_plate
        self.client_cpf = client_cpf
        self.car_id = car_id
        self.client_id = client_id

    def __repr__(self):
        return f"Rent(car_plate={self.car_plate!r}, client_cpf={self.client_cpf!r})"
