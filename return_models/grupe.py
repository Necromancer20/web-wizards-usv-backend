from uuid import UUID

from pydantic import BaseModel, Field, validator


# Model pentru obținerea unei grupă
class GrupeGet(BaseModel):
    id: UUID
    id_facultate: UUID
    id_specializare: UUID
    an: int
    numar_grupa: int
    litera_semigrupa: int


# Model pentru crearea unei grupă
class GrupeCreate(BaseModel):
    id_facultate: UUID
    id_specializare: UUID
    an: int = Field(..., ge=1, le=6, description="Anul trebuie să fie între 1 și 6.")
    numar_grupa: int = Field(..., ge=1, le=99, description="Numărul grupei trebuie să fie între 1 și 99.")
    litera_semigrupa: int = Field(..., ge=1, le=3, description="Litera semigrupa trebuie să fie între 1 și 3.")

    @validator("an")
    def valideaza_an(cls, value):
        if not 1 <= value <= 6:
            raise ValueError("Anul trebuie să fie între 1 și 6.")
        return value


# Model pentru actualizarea unei grupă
class GrupeUpdate(BaseModel):
    id_facultate: UUID
    id_specializare: UUID
    an: int = Field(..., ge=1, le=6, description="Anul trebuie să fie între 1 și 6.")
    numar_grupa: int = Field(..., ge=1, le=99, description="Numărul grupei trebuie să fie între 1 și 99.")
    litera_semigrupa: int = Field(..., ge=1, le=3, description="Litera semigrupa trebuie să fie între 1 și 3.")

    @validator("an")
    def valideaza_an(cls, value):
        if not 1 <= value <= 6:
            raise ValueError("Anul trebuie să fie între 1 și 6.")
        return value
