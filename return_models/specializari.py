from uuid import UUID

from pydantic import BaseModel, Field, validator


# Model pentru obținerea detaliilor unei specializări
class SpecializareGet(BaseModel):
    id: UUID
    id_facultate: UUID
    nume: str


# Model pentru actualizarea unei specializări existente
class SpecializareUpdate(BaseModel):
    id_facultate: UUID
    nume: str = Field(..., min_length=2, max_length=100)

    @validator("nume")
    def valideaza_nume(cls, value):
        if not value.isalpha() or not value.replace(" ", "").isalpha():
            raise ValueError("Numele specializării trebuie să conțină doar litere și spații.")
        return value


# Model pentru crearea unei noi specializări
class SpecializareCreate(BaseModel):
    id_facultate: UUID
    nume: str = Field(..., min_length=2, max_length=100)

    @validator("nume")
    def valideaza_nume(cls, value):
        if not value.isalpha() or not value.replace(" ", "").isalpha():
            raise ValueError("Numele specializării trebuie să conțină doar litere și spații.")
        return value
