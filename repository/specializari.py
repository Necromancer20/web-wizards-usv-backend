import uuid
from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.database import DATABASE_ENGINE
from database.models import Specializari
from return_models.specializari import SpecializareUpdate, SpecializareCreate


# Funcție pentru obținerea unei specializări după ID
def get_specializare_by_id(specializare_id: uuid.UUID) -> Optional[Specializari]:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Specializari).where(Specializari.id == specializare_id)
        specializare = session.scalar(stmt)
        return specializare


# Funcție pentru obținerea tuturor specializărilor
def get_all_specializari() -> List[Specializari]:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Specializari)
        specializari = session.scalars(stmt).all()
        return specializari


# Funcție pentru actualizarea unei specializări existente
def update_specializare_in_db(specializare_id: uuid.UUID, updated_data: SpecializareUpdate) -> bool:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Specializari).where(Specializari.id == specializare_id)
        specializare = session.scalar(stmt)

        if specializare is None:
            return False

        specializare.id_facultate = updated_data.id_facultate
        specializare.nume = updated_data.nume

        session.commit()
        return True


# Funcție pentru ștergerea unei specializări existente
def delete_specializare_by_id(specializare_id: uuid.UUID) -> bool:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Specializari).where(Specializari.id == specializare_id)
        specializare = session.scalar(stmt)

        if specializare is None:
            return False

        session.delete(specializare)
        session.commit()
        return True


# Funcție pentru adăugarea unei noi specializări în DB
def add_specializare_to_db(new_specializare: SpecializareCreate) -> Specializari:
    with Session(DATABASE_ENGINE) as session:
        specializare = Specializari(
            id=uuid.uuid4(),
            id_facultate=new_specializare.id_facultate,
            nume=new_specializare.nume
        )
        session.add(specializare)
        session.commit()
        session.refresh(specializare)
        return specializare
