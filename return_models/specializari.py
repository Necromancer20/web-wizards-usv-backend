from uuid import UUID

from pydantic import BaseModel


# Model pentru obținerea detaliilor unei specializări
class SpecializareGet(BaseModel):
    id: UUID
    id_facultate: UUID
    nume: str


# Model pentru actualizarea unei specializări existente
class SpecializareUpdate(BaseModel):
    id_facultate: UUID
    nume: str


# Model pentru crearea unei noi specializări
class SpecializareCreate(BaseModel):
    id_facultate: UUID
    nume: str
