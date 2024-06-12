from pydantic import  Field, PositiveFloat
from typing import Annotated

from workout_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome atleta', examples=['Joao'], max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', examples=['00000000000'], max_length=11)]
    int: Annotated[int, Field(description='Idade do atleta', examples=[25])]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', examples=[70.5])]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta em metros', examples=[1.70])]
    sexo: Annotated[str, Field(description="Sexo do atleta", max_length=1)]

class AtletaIn(Atleta):
    pass
class AtletaOut(Atleta, OutMixin):
    pass

