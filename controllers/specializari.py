import uuid

from fastapi import APIRouter, HTTPException, status

from database.models import Specializari
from repository.specializari import get_specializare_by_id, get_all_specializari, update_specializare_in_db, \
    delete_specializare_by_id, add_specializare_to_db
from return_models.specializari import SpecializareGet, SpecializareUpdate, SpecializareCreate

router_specializari = APIRouter(
    prefix="/specializari",
    tags=["Specializari"]
)


def _map_specializare(db_specializare: Specializari) -> SpecializareGet:
    return SpecializareGet(
        id=db_specializare.id,
        id_facultate=db_specializare.id_facultate,
        nume=db_specializare.nume
    )


@router_specializari.get("/")
async def get_all_specializari_endpoint() -> list[SpecializareGet]:
    """
    Endpoint pentru obținerea tuturor specializărilor
    """
    return [_map_specializare(s) for s in get_all_specializari()]


@router_specializari.get("/{specializare_id}")
async def get_specializare(specializare_id: uuid.UUID) -> SpecializareGet:
    """
    Endpoint pentru obținerea unei specializări după ID
    """
    specializare = get_specializare_by_id(specializare_id)

    if specializare is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Specialization not found.")

    return _map_specializare(specializare)


@router_specializari.post("/")
async def create_specializare(new_specializare: SpecializareCreate) -> SpecializareGet:
    """
    Endpoint pentru crearea unei noi specializări
    """
    specializare = add_specializare_to_db(new_specializare)
    return _map_specializare(specializare)


@router_specializari.put("/{specializare_id}")
async def update_specializare(specializare_id: uuid.UUID, updated_data: SpecializareUpdate):
    """
    Endpoint pentru actualizarea unei specializări existente
    """
    success = update_specializare_in_db(specializare_id, updated_data)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Specialization not found.")


@router_specializari.delete("/{specializare_id}", status_code=200)
async def delete_specializare(specializare_id: uuid.UUID):
    """
    Endpoint pentru ștergerea unei specializări existente
    """
    success = delete_specializare_by_id(specializare_id)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Specialization not found.")
