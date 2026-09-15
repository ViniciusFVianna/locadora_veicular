import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_DIR = PROJECT_ROOT / "database"
DB_PATH = DB_DIR / "locadora.db"


def get_connection() -> sqlite3.Connection:
    DB_DIR.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    connection = get_connection()
    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cpf TEXT UNIQUE NOT NULL,
                nome TEXT NOT NULL
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS veiculos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                placa TEXT UNIQUE NOT NULL,
                modelo TEXT NOT NULL,
                disponivel INTEGER NOT NULL DEFAULT 1
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS locacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                veiculo_id INTEGER NOT NULL,
                status TEXT NOT NULL DEFAULT 'ativa',
                FOREIGN KEY (cliente_id) REFERENCES clientes(id),
                FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
            )
            """
        )
        connection.commit()
    finally:
        connection.close()
