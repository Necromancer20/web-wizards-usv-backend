import uuid

from fastapi import APIRouter, HTTPException, status

from database.models import Materii
from repository.materii import get_materie_by_id, get_all_materii_from_db, create_materie_in_db, update_materie_in_db, delete_materie_by_id
from return_models.materii import MateriiGet, MateriiCreate, MateriiUpdate

router_materii = APIRouter(
    prefix="/materii",
    tags=["Materii"]
)


def _map_materie(db_materie: Materii) -> MateriiGet:
    return MateriiGet(
        id=db_materie.id,
        id_grupa=db_materie.id_grupa,
        id_profesor=db_materie.id_profesor,
        semestrul=db_materie.semestrul,
        nume=db_materie.nume,
        nume_abreviat=db_materie.nume_abreviat,
        numar_credite=db_materie.numar_credite,
        durata_examen_minute=db_materie.durata_examen_minute
    )


@router_materii.get("/")
async def get_all_materii() -> list[MateriiGet]:
    """
    Endpoint pentru obținerea tuturor materiilor
    """
    materii = get_all_materii_from_db()
    return [_map_materie(materie) for materie in materii]


@router_materii.get("/{materie_id}")
async def get_materie(materie_id: uuid.UUID) -> MateriiGet:
    """
    Endpoint pentru obținerea unei materii după ID
    """
    materie = get_materie_by_id(materie_id)

    if materie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Materie not found")

    return _map_materie(materie)


@router_materii.post("/", status_code=status.HTTP_201_CREATED)
async def create_materie(materie: MateriiCreate):
    """
    Endpoint pentru crearea unei materii noi
    """
    new_materie = create_materie_in_db(materie)

    if not new_materie:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Error creating the materie")

    return _map_materie(new_materie)


@router_materii.put("/{materie_id}")
async def update_materie(materie_id: uuid.UUID, materie: MateriiUpdate):
    """
    Endpoint pentru actualizarea unei materii existente
    """
    success = update_materie_in_db(materie_id, materie)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Materie not found")

    return {"message": "Materie updated successfully"}


@router_materii.delete("/{materie_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_materie(materie_id: uuid.UUID):
    """
    Endpoint pentru ștergerea unei materii existente
    """
    success = delete_materie_by_id(materie_id)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Materie not found")
