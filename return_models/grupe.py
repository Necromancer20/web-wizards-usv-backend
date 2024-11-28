from uuid import UUID

from pydantic import BaseModel


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
    an: int
    numar_grupa: int
    litera_semigrupa: int


# Model pentru actualizarea unei grupă
class GrupeUpdate(BaseModel):
    id_facultate: UUID
    id_specializare: UUID
    an: int
    numar_grupa: int
    litera_semigrupa: int
