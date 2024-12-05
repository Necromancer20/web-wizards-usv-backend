from uuid import UUID

from pydantic import BaseModel, Field


# Model pentru obținerea unei facultăți
class FacultateGet(BaseModel):
    id: UUID
    nume_facultate: str


# Model pentru crearea unei facultăți
class FacultateCreate(BaseModel):
    nume_facultate: str = Field(..., min_length=2, max_length=100, description="Numele facultății trebuie să aibă între 2 și 100 de caractere.")


# Model pentru actualizarea unei facultăți
class FacultateUpdate(BaseModel):
    nume_facultate: str = Field(..., min_length=2, max_length=100, description="Numele facultății trebuie să aibă între 2 și 100 de caractere.")
