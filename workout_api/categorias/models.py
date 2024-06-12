from datetime import datetime
from pydantic import UUID4
from sqlalchemy import Integer, String, DateTime, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel

class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id: Mapped[UUID4] = mapped_column(UUID, unique=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    atletas: Mapped['AtletaModel'] = relationship(back_populates='categoria')
