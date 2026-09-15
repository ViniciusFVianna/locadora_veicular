from typing import Optional

from locadora_veicular.core.database import get_connection
from locadora_veicular.models.cliente import Cliente


class ClienteRepository:
    def save(self, cliente: Cliente) -> Cliente:
        with get_connection() as connection:
            cursor = connection.execute(
                "INSERT INTO clientes (cpf, nome) VALUES (?, ?)",
                (cliente.cpf, cliente.nome),
            )
            cliente.id = cursor.lastrowid
            connection.commit()
        return cliente

    def list_all(self) -> list[Cliente]:
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, cpf, nome FROM clientes ORDER BY id"
            ).fetchall()
        return [Cliente(id=row["id"], cpf=row["cpf"], nome=row["nome"]) for row in rows]

    def find_by_cpf(self, cpf: str) -> Optional[Cliente]:
        with get_connection() as connection:
            row = connection.execute(
                "SELECT id, cpf, nome FROM clientes WHERE cpf = ?",
                (cpf,),
            ).fetchone()
        if row is None:
            return None
        return Cliente(id=row["id"], cpf=row["cpf"], nome=row["nome"])
