from typing import Optional

from locadora_veicular.core.database import get_connection
from locadora_veicular.models.veiculo import Veiculo


class VeiculoRepository:
    def save(self, veiculo: Veiculo) -> Veiculo:
        with get_connection() as connection:
            cursor = connection.execute(
                "INSERT INTO veiculos (placa, modelo, disponivel) VALUES (?, ?, ?)",
                (veiculo.placa, veiculo.modelo, int(veiculo.disponivel)),
            )
            veiculo.id = cursor.lastrowid
            connection.commit()
        return veiculo

    def list_all(self) -> list[Veiculo]:
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, placa, modelo, disponivel FROM veiculos ORDER BY id"
            ).fetchall()
        return [
            Veiculo(
                id=row["id"],
                placa=row["placa"],
                modelo=row["modelo"],
                disponivel=bool(row["disponivel"]),
            )
            for row in rows
        ]

    def find_by_placa(self, placa: str) -> Optional[Veiculo]:
        with get_connection() as connection:
            row = connection.execute(
                "SELECT id, placa, modelo, disponivel FROM veiculos WHERE placa = ?",
                (placa,),
            ).fetchone()
        if row is None:
            return None
        return Veiculo(
            id=row["id"],
            placa=row["placa"],
            modelo=row["modelo"],
            disponivel=bool(row["disponivel"]),
        )

    def update(self, veiculo: Veiculo) -> None:
        with get_connection() as connection:
            connection.execute(
                "UPDATE veiculos SET placa = ?, modelo = ?, disponivel = ? WHERE id = ?",
                (veiculo.placa, veiculo.modelo, int(veiculo.disponivel), veiculo.id),
            )
            connection.commit()
