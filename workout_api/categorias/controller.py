from uuid import uuid4
from datetime import datetime
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select
from workout_api.categorias.models import CategoriaModel
from workout_api.categorias.schemas import CategoriasIn, CategoriasOut

from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(
    '/',
    summary='Cria uma nova Categoria',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriasOut
)
async def post(
    db_session: DatabaseDependency,
    catgoria_in: CategoriasIn = Body(...) 
) -> CategoriasOut:
    categorias_out = CategoriasOut(id=uuid4(), created_at=datetime.now(), **catgoria_in.model_dump())

    categoria_model = CategoriaModel(**categorias_out.model_dump())

    db_session.add(categoria_model)

    await db_session.commit()

    return categorias_out

@router.get(
    '/',
    summary='consultar todas as categorias disponíveis',
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriasOut]
)
async def query(
    db_session: DatabaseDependency
) -> list[CategoriasOut] :
    categorias: list[CategoriasOut] = (
        await db_session.execute(select(CategoriaModel))
    ).scalars().all()

    return categorias

@router.get(
    '/{id}',
    summary='Consulta categoria',
    status_code=status.HTTP_200_OK,
    response_model=CategoriasOut
)
async def query(
    id: UUID4,
    db_session: DatabaseDependency
) -> CategoriasOut:
    
    categoria: CategoriasOut = (
        await db_session.execute(
            select(CategoriaModel).filter_by(id=id)
        )
    ).scalars().first()

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Categoria não encontrada id: {id}'
        )

    return categoria
