"""Camada de infraestrutura e configuração local do sistema.

Responsável pela conexão com o banco SQLite e pela inicialização das
estruturas básicas de persistência da aplicação.
"""

from .database import get_connection, init_db

__all__ = ["get_connection", "init_db"]
