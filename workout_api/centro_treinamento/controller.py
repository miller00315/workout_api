from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status

from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(
    '/',
    summary='Criar um novo centro de treinamento',
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def post(
    db_session: DatabaseDependency,
    centro_treinamento_in: CentroTreinamentoIn = Body(...)
):
    centro_treinamento_out = CentroTreinamentoOut(
        id=uuid4(), 
        created_at=datetime.now(), 
        **centro_treinamento_in.model_dump()
    )

    centro_treinamento_model = CentroTreinamentoModel(
        **centro_treinamento_out.model_dump(),
    )

    db_session.add(centro_treinamento_model)

    await db_session.commit()

    return centro_treinamento_out

