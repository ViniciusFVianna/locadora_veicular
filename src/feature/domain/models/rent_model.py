from datetime import datetime

class RentModel:
    def __init__(self, cpf_cliente, placa_carro, dias, valor_total, id=None, data=None, ativa=True):
        self.id = id
        self.cpf_cliente = cpf_cliente = cpf_cliente
        self.placa_carro = placa_carro = placa_carro
        self.dias = dias = int(dias)
        self.valor_total = valor_total = float(valor_total)
        self.data = data = data if data else datetime.now().strftime("%d/%m/%Y %H:%M")
        self.ativa = ativa = ativa

    def to_dict(self):
        return {
            "id": self.id,
            "cpf_cliente": self.cpf_cliente,
            "placa_carro": self.placa_carro,
            "dias": self.dias,
            "valor_total": self.valor_total,
            "data": self.data,
            "ativa": self.ativa
        }
