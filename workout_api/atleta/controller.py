from fastapi import APIRouter, Body, status

from workout_api.atleta.schemas import AtletaIn, AtletaOut
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(
    path='/',
    summary='Criar um novo atleta',
    status_code=status.HTTP_201_CREATED
)
async def post(
    db_session: DatabaseDependency,
    atleta_in: AtletaIn = Body(...)
) -> AtletaOut:
    pass

