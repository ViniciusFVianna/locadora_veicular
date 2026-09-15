"""Entidades do sistema de locadora.

Este pacote reúne as estruturas centrais do domínio, representando clientes
veículos e demais conceitos relacionados à operação da locadora.
"""

from .cliente import Cliente
from .veiculo import Veiculo

__all__ = ["Cliente", "Veiculo"]
