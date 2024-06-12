from datetime import datetime
from pydantic import UUID4
from sqlalchemy import UUID, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel

class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamento'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id: Mapped[UUID4] = mapped_column(UUID, unique=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    atletas: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')
