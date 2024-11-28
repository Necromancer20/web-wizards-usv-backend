from uuid import UUID

from pydantic import BaseModel


# Model pentru obținerea unei facultăți
class FacultateGet(BaseModel):
    id: UUID
    nume_facultate: str


# Model pentru crearea unei facultăți
class FacultateCreate(BaseModel):
    nume_facultate: str


# Model pentru actualizarea unei facultăți
class FacultateUpdate(BaseModel):
    nume_facultate: str
