from uuid import UUID

from pydantic import BaseModel


class UtilizatorLogin(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str
    rol: str


class UtilizatorGet(UtilizatorLogin):
    pass


class UtilizatorUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str
    parola: str
    rol: str
