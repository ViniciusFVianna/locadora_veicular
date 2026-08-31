class Car:
    def __init__(self, plate, model, disponibility=True, id=None):
        self.id = id
        self.plate = plate
        self.model = model
        self.disponibility = disponibility

    def __repr__(self):
        return f"Car(plate={self.plate!r}, model={self.model!r}, disponibility={self.disponibility!r})"
