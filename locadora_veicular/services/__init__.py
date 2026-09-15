"""Serviços de negócio da locadora.

A camada de serviços concentra as regras de negócio, como validações e
operações relacionadas à locação e devolução de veículos.
"""

from .locacao_service import LocacaoService

__all__ = ["LocacaoService"]
