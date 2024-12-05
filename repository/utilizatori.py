import uuid
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.database import DATABASE_ENGINE
from database.models import Utilizator
from return_models.utilizatori import UtilizatorUpdate, UtilizatorCreate


def get_user_by_email(email: str) -> Optional[Utilizator]:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Utilizator).where(Utilizator.email == email)

        utilizator = session.scalar(stmt)

        return utilizator


def get_user_by_id(user_id: uuid.UUID) -> Optional[Utilizator]:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Utilizator).where(Utilizator.id == user_id)

        utilizator = session.scalar(stmt)
        return utilizator


def get_all_users_from_db() -> list[Utilizator]:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Utilizator)

        utilizator = session.scalars(stmt).all()

        return utilizator


def delete_user_by_id(user_id: uuid.UUID) -> bool:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Utilizator).where(Utilizator.id == user_id)

        utilizator = session.scalar(stmt)

        if utilizator is None:
            return False

        session.delete(utilizator)
        session.commit()

        return True


def update_user_in_db(user_id: uuid.UUID, new_user: UtilizatorUpdate) -> bool:
    with Session(DATABASE_ENGINE) as session:
        stmt = select(Utilizator).where(Utilizator.id == user_id)

        utilizator = session.scalar(stmt)

        if utilizator is None:
            return False

        utilizator.password = new_user.parola
        utilizator.email = new_user.email
        utilizator.first_name = new_user.first_name
        utilizator.last_name = new_user.last_name
        utilizator.rol = new_user.rol

        session.commit()

        return True


def add_user_to_db(new_user: UtilizatorCreate) -> Utilizator:
    with Session(DATABASE_ENGINE) as session:
        utilizator = Utilizator(
            id=uuid.uuid4(),
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            email=new_user.email,
            password=new_user.password,
            rol=new_user.rol
        )
        session.add(utilizator)
        session.commit()
        session.refresh(utilizator)
        return utilizator
