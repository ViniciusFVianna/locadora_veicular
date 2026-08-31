class Client:
    def __init__(self, cpf, name, id=None):
        self.id = id
        self.cpf = cpf
        self.name = name

    def __repr__(self):
        return f"Client(cpf={self.cpf!r}, name={self.name!r})"
