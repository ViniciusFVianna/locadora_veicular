class Carro:
    def __init__(self, marca, modelo, ano, placa, cor, quilometragem, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.cor = cor
        self.quilometragem = quilometragem
        self.preco = preco
    def to_dict(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "ano": self.ano,
            "placa": self.placa,
            "cor": self.cor,
            "quilometragem": self.quilometragem,
            "preco": self.preco
        }