"""Este módulo contém o contrato de dados que \
    define a tabela de Metas da empresa."""

from datetime import datetime

from pydantic import BaseModel, PositiveFloat


class Metas(BaseModel):
    """Modelo de tabela de metas.

    Args:
        data (datetime): data da compra
        vendedor (str): vendedor da empresa
        valor (float): valor da compra
    """

    data: datetime
    vendedor: str
    valor: PositiveFloat
