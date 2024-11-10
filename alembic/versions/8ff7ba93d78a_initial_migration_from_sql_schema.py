"""Initial migration from SQL schema

Revision ID: 8ff7ba93d78a
Revises: 
Create Date: 2024-11-10 12:40:18.500999

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision: str = '8ff7ba93d78a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facultati',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('nume', sa.VARCHAR(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('utilizator',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=30), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=30), nullable=False),
    sa.Column('email', sa.VARCHAR(length=30), nullable=False),
    sa.Column('password', sa.VARCHAR(length=30), nullable=False),
    sa.Column('rol', sa.Enum('ADMIN', 'USER', 'PROFESSOR', name='userrole'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('specializari',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('id_facultate', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('nume', sa.VARCHAR(length=30), nullable=False),
    sa.ForeignKeyConstraint(['id_facultate'], ['facultati.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grupe',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('id_facultate', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('id_specializare', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('an', sa.Integer(), nullable=False),
    sa.Column('numar_grupa', sa.Integer(), nullable=False),
    sa.Column('litera_semigrupa', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_facultate'], ['facultati.id'], ),
    sa.ForeignKeyConstraint(['id_specializare'], ['specializari.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grupe_utilizator',
    sa.Column('id_utilizator', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('id_grupa', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('este_sef_semigrupa', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['id_grupa'], ['grupe.id'], ),
    sa.ForeignKeyConstraint(['id_utilizator'], ['utilizator.id'], ),
    sa.PrimaryKeyConstraint('id_utilizator', 'id_grupa')
    )
    op.create_table('materii',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('id_grupa', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('id_profesor', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('semestrul', sa.Integer(), nullable=False),
    sa.Column('nume', sa.VARCHAR(length=30), nullable=False),
    sa.Column('nume_abreviat', sa.VARCHAR(length=10), nullable=False),
    sa.Column('numar_credite', sa.Integer(), nullable=False),
    sa.Column('durata_examen_minute', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_grupa'], ['grupe.id'], ),
    sa.ForeignKeyConstraint(['id_profesor'], ['utilizator.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('programari_examen',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('id_materie', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('id_profesor', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('id_student_creator', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('id_grupa', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('data_examen', sa.DateTime(), nullable=False),
    sa.Column('locatie', sa.VARCHAR(length=30), nullable=False),
    sa.Column('tip_examen', sa.Enum('ORAL', 'WRITTEN', name='examtype'), nullable=False),
    sa.Column('observatii', sa.Text(), nullable=True),
    sa.Column('status', sa.Enum('ACCEPTAT', 'REFUZAT', 'IN_ASTEPATARE', name='examstatus'), nullable=False),
    sa.ForeignKeyConstraint(['id_grupa'], ['grupe.id'], ),
    sa.ForeignKeyConstraint(['id_materie'], ['materii.id'], ),
    sa.ForeignKeyConstraint(['id_profesor'], ['utilizator.id'], ),
    sa.ForeignKeyConstraint(['id_student_creator'], ['utilizator.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('programari_examen')
    op.drop_table('materii')
    op.drop_table('grupe_utilizator')
    op.drop_table('grupe')
    op.drop_table('specializari')
    op.drop_table('utilizator')
    op.drop_table('facultati')
    # ### end Alembic commands ###
