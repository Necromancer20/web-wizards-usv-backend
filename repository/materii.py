import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.database import DATABASE_ENGINE
from database.models import Materii


# Funcție pentru obținerea unei materii după ID
def get_materie_by_id(materie_id: uuid.UUID) -> Materii:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Materii).where(Materii.id == materie_id)
        materie = session.scalar(stmt)
        return materie


def get_durata_examen_materie_by_id(materie_id: uuid.UUID) -> int:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Materii.durata_examen_minute).where(Materii.id == materie_id)
        durata = session.scalar(stmt)
        return durata


# Funcție pentru obținerea tuturor materiilor
def get_all_materii_from_db() -> list[Materii]:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Materii)
        materii = session.scalars(stmt).all()
        return materii


# Funcție pentru crearea unei materii noi
def create_materie_in_db(materie_data) -> Materii:
    with Session(DATABASE_ENGINE) as session:
        new_materie = Materii(
            id=uuid.uuid4(),
            id_grupa=materie_data.id_grupa,
            id_profesor=materie_data.id_profesor,
            semestrul=materie_data.semestrul,
            nume=materie_data.nume,
            nume_abreviat=materie_data.nume_abreviat,
            numar_credite=materie_data.numar_credite,
            durata_examen_minute=materie_data.durata_examen_minute
        )
        session.add(new_materie)
        session.commit()
        session.refresh(new_materie)
        return new_materie


# Funcție pentru actualizarea unei materii existente
def update_materie_in_db(materie_id: uuid.UUID, materie_data) -> bool:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Materii).where(Materii.id == materie_id)
        materie = session.scalar(stmt)

        if not materie:
            return False

        materie.id_grupa = materie_data.id_grupa
        materie.id_profesor = materie_data.id_profesor
        materie.semestrul = materie_data.semestrul
        materie.nume = materie_data.nume
        materie.nume_abreviat = materie_data.nume_abreviat
        materie.numar_credite = materie_data.numar_credite
        materie.durata_examen_minute = materie_data.durata_examen_minute

        session.commit()
        return True


# Funcție pentru ștergerea unei materii existente
def delete_materie_by_id(materie_id: uuid.UUID) -> bool:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Materii).where(Materii.id == materie_id)
        materie = session.scalar(stmt)

        if not materie:
            return False

        session.delete(materie)
        session.commit()
        return True
