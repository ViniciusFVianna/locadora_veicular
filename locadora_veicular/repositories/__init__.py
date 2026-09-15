"""Repositórios da aplicação.

Responsáveis por encapsular o acesso e manipulação dos dados persistidos em
SQLite, oferecendo operações de criação, leitura, atualização e exclusão.
"""

from .cliente_repository import ClienteRepository
from .veiculo_repository import VeiculoRepository

__all__ = ["ClienteRepository", "VeiculoRepository"]
