from typing import Annotated

from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema, OutMixin

class Categorias(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria', examples=['Scale'], max_length=25)]

class CategoriasIn(Categorias):
    pass

class CategoriasOut(CategoriasIn, OutMixin):
    pass