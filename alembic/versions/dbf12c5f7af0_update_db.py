"""update_db

Revision ID: dbf12c5f7af0
Revises: f4c5a2ca022f
Create Date: 2024-06-12 11:59:41.978934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dbf12c5f7af0'
down_revision: Union[str, None] = 'f4c5a2ca022f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('atletas', sa.Column('CPF', sa.String(length=11), nullable=False))
    op.alter_column('atletas', 'peso',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               existing_nullable=False)
    op.drop_constraint('atletas_cpf_key', 'atletas', type_='unique')
    op.create_unique_constraint(None, 'atletas', ['id'])
    op.create_unique_constraint(None, 'atletas', ['CPF'])
    op.drop_column('atletas', 'cpf')
    op.add_column('categorias', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.create_unique_constraint(None, 'categorias', ['id'])
    op.add_column('centros_treinamento', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.create_unique_constraint(None, 'centros_treinamento', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'centros_treinamento', type_='unique')
    op.drop_column('centros_treinamento', 'created_at')
    op.drop_constraint(None, 'categorias', type_='unique')
    op.drop_column('categorias', 'created_at')
    op.add_column('atletas', sa.Column('cpf', sa.VARCHAR(length=11), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'atletas', type_='unique')
    op.drop_constraint(None, 'atletas', type_='unique')
    op.create_unique_constraint('atletas_cpf_key', 'atletas', ['cpf'])
    op.alter_column('atletas', 'peso',
               existing_type=sa.Integer(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=False)
    op.drop_column('atletas', 'CPF')
    # ### end Alembic commands ###