import uuid

from fastapi import APIRouter, HTTPException, status

from database.models import ProgramariExamen
from repository.programari_examen import get_programare_examen_by_id, get_all_programari_examen_from_db, create_programare_examen_in_db, update_programare_examen_in_db, delete_programare_examen_by_id
from return_models.programari_examen import ProgramareExamenGet, ProgramareExamenCreate, ProgramareExamenUpdate

router_programari_examen = APIRouter(
    prefix="/programari_examen",
    tags=["Programari Examen"]
)


def _map_programare_examen(db_programare_examen: ProgramariExamen) -> ProgramareExamenGet:
    return ProgramareExamenGet(
        id=db_programare_examen.id,
        id_materie=db_programare_examen.id_materie,
        id_profesor=db_programare_examen.id_profesor,
        id_student_creator=db_programare_examen.id_student_creator,
        id_grupa=db_programare_examen.id_grupa,
        data_examen=db_programare_examen.data_examen,
        locatie=db_programare_examen.locatie,
        tip_examen=db_programare_examen.tip_examen,
        observatii=db_programare_examen.observatii,
        status=db_programare_examen.status
    )


@router_programari_examen.get("/")
async def get_all_programari_examen() -> list[ProgramareExamenGet]:
    """
    Endpoint pentru obținerea tuturor programărilor de examen
    """
    programari = get_all_programari_examen_from_db()
    return [_map_programare_examen(programare) for programare in programari]


@router_programari_examen.get("/{programare_id}")
async def get_programare_examen(programare_id: uuid.UUID) -> ProgramareExamenGet:
    """
    Endpoint pentru obținerea unei programări de examen după ID
    """
    programare = get_programare_examen_by_id(programare_id)

    if programare is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Programare examen not found")

    return _map_programare_examen(programare)


@router_programari_examen.get("/filter")
async def filter_programari_examen(id_grupa: uuid.UUID | None = None, id_profesor: uuid.UUID | None = None) -> list[ProgramareExamenGet]:
    """
    Endpoint pentru filtrarea programărilor de examen în funcție de grupă și/sau profesor.
    """
    programari = get_all_programari_examen_from_db()

    if id_grupa:
        programari = [programare for programare in programari if programare.id_grupa == id_grupa]

    if id_profesor:
        programari = [programare for programare in programari if programare.id_profesor == id_profesor]

    return [_map_programare_examen(programare) for programare in programari]



@router_programari_examen.post("/", status_code=status.HTTP_201_CREATED)
async def create_programare_examen(programare: ProgramareExamenCreate):
    """
    Endpoint pentru crearea unei programări de examen
    """
    new_programare_examen = create_programare_examen_in_db(programare)

    if not new_programare_examen:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Error creating the programare examen")

    return _map_programare_examen(new_programare_examen)


@router_programari_examen.put("/{programare_id}")
async def update_programare_examen(programare_id: uuid.UUID, programare: ProgramareExamenUpdate):
    """
    Endpoint pentru actualizarea unei programări de examen existente
    """
    success = update_programare_examen_in_db(programare_id, programare)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Programare examen not found")

    return {"message": "Programare examen updated successfully"}


@router_programari_examen.delete("/{programare_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_programare_examen(programare_id: uuid.UUID):
    """
    Endpoint pentru ștergerea unei programări de examen existente
    """
    success = delete_programare_examen_by_id(programare_id)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Programare examen not found")
