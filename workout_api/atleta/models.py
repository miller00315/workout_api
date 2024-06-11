from datetime import datetime
from sqlalchemy import Integer, String, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from contrib.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__ = 'atleta'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    CPF: Mapped[str] = mapped_column(String(11), nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[int] = mapped_column(Integer, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
