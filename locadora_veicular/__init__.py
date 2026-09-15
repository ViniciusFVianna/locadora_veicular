"""Pacote principal da locadora veicular.

Este pacote expõe a fachada pública da aplicação e centraliza a
organização das camadas de domínio, acesso a dados e regras de negócio.
"""

from .core.database import get_connection
from .models.cliente import Cliente
from .models.veiculo import Veiculo

__all__ = ["Cliente", "Veiculo", "get_connection"]
