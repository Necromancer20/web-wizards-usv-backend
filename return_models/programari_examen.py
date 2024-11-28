from uuid import UUID

from pydantic import BaseModel

from datetime import datetime
from enum import Enum
from typing import Optional


# Enum pentru tipul examenului
class ExamType(str, Enum):
    EXAMEN = "examen"
    COLOCVIU = "colocviu"


# Enum pentru statusul examenului
class ExamStatus(str, Enum):
    ACCEPTAT = "aceptat"
    REFUZAT = "refuzat"
    IN_ASTEPTARE = "in_asteptare"


# Model pentru obținerea detaliilor unei programări de examen
class ProgramareExamenGet(BaseModel):
    id: UUID
    id_materie: UUID
    id_profesor: UUID
    id_student_creator: UUID
    id_grupa: UUID
    data_examen: datetime
    locatie: str
    tip_examen: ExamType
    observatii: Optional[str] = None
    status: ExamStatus


# Model pentru crearea unei programări de examen
class ProgramareExamenCreate(BaseModel):
    id_materie: UUID
    id_profesor: UUID
    id_student_creator: UUID
    id_grupa: UUID
    data_examen: datetime
    locatie: str
    tip_examen: ExamType
    observatii: Optional[str] = None
    status: ExamStatus


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
