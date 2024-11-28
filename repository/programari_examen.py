import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.database import DATABASE_ENGINE
from database.models import ProgramariExamen


# Funcție pentru obținerea unei programări de examen după ID
def get_programare_examen_by_id(programare_id: uuid.UUID) -> ProgramariExamen:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(ProgramariExamen).where(ProgramariExamen.id == programare_id)
        programare = session.scalar(stmt)
        return programare


# Funcție pentru obținerea tuturor programărilor de examen
def get_all_programari_examen_from_db() -> list[ProgramariExamen]:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(ProgramariExamen)
        programari = session.scalars(stmt).all()
        return programari


# Funcție pentru crearea unei programări de examen noi
def create_programare_examen_in_db(programare_data) -> ProgramariExamen:
    with Session(DATABASE_ENGINE) as session:
        new_programare_examen = ProgramariExamen(**programare_data.dict())
        session.add(new_programare_examen)
        session.commit()
        session.refresh(new_programare_examen)
        return new_programare_examen


# Funcție pentru actualizarea unei programări de examen existente
def update_programare_examen_in_db(programare_id: uuid.UUID, programare_data) -> bool:
    with Session(DATABASE_ENGINE) as session:
        programare = session.get(ProgramariExamen, programare_id)

        if not programare:
            return False

        for key, value in programare_data.dict(exclude_unset=True).items():
            setattr(programare, key, value)

        session.commit()
        return True


# Funcție pentru ștergerea unei programări de examen existente
def delete_programare_examen_by_id(programare_id: uuid.UUID) -> bool:
    with Session(DATABASE_ENGINE) as session:
        programare = session.get(ProgramariExamen, programare_id)

        if not programare:
            return False

        session.delete(programare)
        session.commit()
        return True
