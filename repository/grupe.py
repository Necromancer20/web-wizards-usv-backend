import uuid
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.database import DATABASE_ENGINE
from database.models import Grupe, GrupeUtilizator


# Funcție pentru obținerea unei grupe după ID
def get_grupa_by_id(grupa_id: uuid.UUID) -> Grupe:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Grupe).where(Grupe.id == grupa_id)
        grupa = session.scalar(stmt)
        return grupa


def get_grupa_utilizator(user_id: uuid.UUID) -> Optional[tuple[uuid.UUID, bool]]:
    with Session(DATABASE_ENGINE) as session:
        stmt = (
            select(GrupeUtilizator)
            .where(GrupeUtilizator.id_utilizator == user_id)
        )
        data = session.scalar(stmt)

        if not data:
            return None

        return data.id_grupa, data.este_sef_semigrupa


# Funcție pentru obținerea tuturor grupelor
def get_all_grupe_from_db() -> list[Grupe]:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Grupe)
        grupe = session.scalars(stmt).all()
        return grupe


# Funcție pentru crearea unei grupe
def create_grupa_in_db(grupa_data) -> Grupe:
    with Session(DATABASE_ENGINE) as session:
        new_grupa = Grupe(id=uuid.uuid4(), **grupa_data.dict())
        session.add(new_grupa)
        session.commit()
        session.refresh(new_grupa)
        return new_grupa


# Funcție pentru actualizarea unei grupe
def update_grupa_in_db(grupa_id: uuid.UUID, grupa_data) -> bool:
    with Session(DATABASE_ENGINE) as session:
        grupa = session.get(Grupe, grupa_id)

        if not grupa:
            return False

        for key, value in grupa_data.dict(exclude_unset=True).items():
            setattr(grupa, key, value)

        session.commit()
        return True


# Funcție pentru ștergerea unei grupe
def delete_grupa_by_id(grupa_id: uuid.UUID) -> bool:
    with Session(DATABASE_ENGINE) as session:
        grupa = session.get(Grupe, grupa_id)

        if not grupa:
            return False

        session.delete(grupa)
        session.commit()
        return True
