from dataclasses import dataclass
from typing import Optional


@dataclass
class Veiculo:
    placa: str
    modelo: str
    disponivel: bool = True
    id: Optional[int] = None

    def __str__(self) -> str:
        return f"Veiculo(placa={self.placa}, modelo={self.modelo}, disponivel={self.disponivel})"
