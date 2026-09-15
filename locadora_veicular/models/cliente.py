from dataclasses import dataclass
from typing import Optional


@dataclass
class Cliente:
    cpf: str
    nome: str
    id: Optional[int] = None

    def __str__(self) -> str:
        return f"Cliente(cpf={self.cpf}, nome={self.nome})"
