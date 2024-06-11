from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated

class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome atleta', examples='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', examples='00000000000', max_length=11)]
    int: Annotated[int, Field(description='Idade do atleta', examples=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', examples=70.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta em metros', examples=1.70)]
    sexo: Annotated[str, Field(description="Sexo do atlta", max_length=1)]
    