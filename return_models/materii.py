from uuid import UUID

from pydantic import BaseModel


# Model pentru obținerea unei materii
class MateriiGet(BaseModel):
    id: UUID
    id_grupa: UUID
    id_profesor: UUID
    semestrul: int
    nume: str
    nume_abreviat: str
    numar_credite: int
    durata_examen_minute: int


# Model pentru crearea unei materii
class MateriiCreate(BaseModel):
    id_grupa: UUID
    id_profesor: UUID
    semestrul: int
    nume: str
    nume_abreviat: str
    numar_credite: int
    durata_examen_minute: int


# Model pentru actualizarea unei materii
class MateriiUpdate(BaseModel):
    id_grupa: UUID
    id_profesor: UUID
    semestrul: int
    nume: str
    nume_abreviat: str
    numar_credite: int
    durata_examen_minute: int
