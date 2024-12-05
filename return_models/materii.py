from uuid import UUID

from pydantic import BaseModel, Field, validator


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
    semestrul: int = Field(..., ge=1, le=2, description="Semestrul trebuie să fie 1 sau 2.")
    nume: str = Field(..., min_length=2, max_length=100, description="Numele trebuie să aibă între 2 și 100 de caractere.")
    nume_abreviat: str = Field(..., min_length=1, max_length=10, description="Numele abreviat trebuie să aibă între 1 și 10 caractere.")
    numar_credite: int = Field(..., gt=0, description="Numărul de credite trebuie să fie pozitiv.")
    durata_examen_minute: int = Field(..., gt=0, description="Durata examenului (în minute) trebuie să fie pozitivă.")

    @validator("nume")
    def valideaza_nume(cls, value):
        if not value.isalpha():
            raise ValueError("Numele trebuie să conțină doar litere.")
        return value

    @validator("nume_abreviat")
    def valideaza_nume_abreviat(cls, value):
        if not value.isalnum():
            raise ValueError("Numele abreviat trebuie să conțină doar litere și cifre.")
        return value


# Model pentru actualizarea unei materii
class MateriiUpdate(BaseModel):
    id_grupa: UUID
    id_profesor: UUID
    semestrul: int = Field(..., ge=1, le=2, description="Semestrul trebuie să fie 1 sau 2.")
    nume: str = Field(..., min_length=2, max_length=100, description="Numele trebuie să aibă între 2 și 100 de caractere.")
    nume_abreviat: str = Field(..., min_length=1, max_length=10, description="Numele abreviat trebuie să aibă între 1 și 10 caractere.")
    numar_credite: int = Field(..., gt=0, description="Numărul de credite trebuie să fie pozitiv.")
    durata_examen_minute: int = Field(..., gt=0, description="Durata examenului (în minute) trebuie să fie pozitivă.")

    @validator("nume")
    def valideaza_nume(cls, value):
        if not value.isalpha():
            raise ValueError("Numele trebuie să conțină doar litere.")
        return value

    @validator("nume_abreviat")
    def valideaza_nume_abreviat(cls, value):
        if not value.isalnum():
            raise ValueError("Numele abreviat trebuie să conțină doar litere și cifre.")
        return value
