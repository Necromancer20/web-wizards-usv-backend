import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.database import DATABASE_ENGINE
from database.models import Facultati


# Funcție pentru obținerea unei facultăți după ID
def get_facultate_by_id(facultate_id: uuid.UUID) -> Facultati:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Facultati).where(Facultati.id == facultate_id)
        facultate = session.scalar(stmt)
        return facultate


# Funcție pentru obținerea tuturor facultăților
def get_all_facultati_from_db() -> list[Facultati]:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Facultati)
        facultati = session.scalars(stmt).all()
        return facultati


# Funcție pentru crearea unei noi facultăți
def create_facultate_in_db(facultate_data) -> Facultati:
    with Session(DATABASE_ENGINE) as session:
        new_facultate = Facultati(
            id=uuid.uuid4(),
            nume=facultate_data.nume_facultate,
        )
        session.add(new_facultate)
        session.commit()
        session.refresh(new_facultate)
        return new_facultate


# Funcție pentru actualizarea unei facultăți existente
def update_facultate_in_db(facultate_id: uuid.UUID, facultate_data) -> bool:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Facultati).where(Facultati.id == facultate_id)
        facultate = session.scalar(stmt)

        if not facultate:
            return False

        facultate.nume = facultate_data.nume_facultate

        session.commit()
        return True


# Funcție pentru ștergerea unei facultăți existente
def delete_facultate_by_id(facultate_id: uuid.UUID) -> bool:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Facultati).where(Facultati.id == facultate_id)
        facultate = session.scalar(stmt)

        if not facultate:
            return False

        session.delete(facultate)
        session.commit()
        return True
