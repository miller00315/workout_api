from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', examples=['Centro vila ema'], max_length=50)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', examples=['Avenida exemplo, Q01'], max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', examples=['Paulo'], max_length=30)]