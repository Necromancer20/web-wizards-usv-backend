from uuid import UUID

from pydantic import BaseModel, Field, validator
from repository.programari_examen import check_examen_grupa_distanta_minima
from datetime import datetime, UTC
from enum import Enum
from typing import Optional

from database.models import ExamType, ExamStatus


# Model pentru obținerea detaliilor unei programări de examen
class ProgramareExamenGet(BaseModel):
    id: UUID
    id_materie: UUID
    id_profesor: UUID
    id_student_creator: UUID
    id_grupa: UUID
    data_examen: datetime
    data_finalizare_examen: datetime
    locatie: str = Field(..., min_length=2, max_length=100)
    tip_examen: ExamType
    observatii: Optional[str] = None
    status: ExamStatus
    durata_examen_minute: int


# Model pentru crearea unei programări de examen
class ProgramareExamenCreate(BaseModel):
    id_materie: UUID
    id_profesor: UUID
    id_student_creator: UUID
    id_grupa: UUID
    data_examen: datetime
    locatie: str = Field(..., min_length=2, max_length=100)
    tip_examen: ExamType
    observatii: Optional[str] = None
    status: ExamStatus

    @validator("data_examen")
    def valideaza_data_examen(cls, value, values):
        # Verificăm dacă data examenului este în viitor
        if value <= datetime.now(UTC):
            raise ValueError("Data examenului trebuie să fie în viitor.")

        # Verificăm dacă există examene prea aproape de examenul curent
        id_grupa = values.get('id_grupa')
        if id_grupa and not check_examen_grupa_distanta_minima(id_grupa, value):
            raise ValueError(
                "Nu poți programa un examen mai devreme de 2 zile față de alte examene ale aceleași grupe.")

        return value

    @validator("locatie")
    def valideaza_locatie(cls, value):
        if not value.replace(" ", "").isalnum():
            raise ValueError("Locația poate conține doar litere, cifre și spații.")
        return value


# Model pentru actualizarea unei programări de examen
class ProgramareExamenUpdate(BaseModel):
    id_materie: UUID
    id_profesor: UUID
    id_student_creator: UUID
    id_grupa: UUID
    data_examen: datetime
    locatie: str
    tip_examen: ExamType
    observatii: Optional[str] = None
    status: ExamStatus

    @validator("data_examen")
    def valideaza_data_examen(cls, value):
        if value <= datetime.now(UTC):
            raise ValueError("Data examenului trebuie să fie în viitor.")
        return value

    @validator("locatie")
    def valideaza_locatie(cls, value):
        if not value.replace(" ", "").isalnum():
            raise ValueError("Locația poate conține doar litere, cifre și spații.")
        return value
