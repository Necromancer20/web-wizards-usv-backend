import uuid

from fastapi import APIRouter, HTTPException, status

from database.models import Facultati
from repository.facultati import get_facultate_by_id, get_all_facultati_from_db, create_facultate_in_db, update_facultate_in_db, delete_facultate_by_id
from return_models.facultati import FacultateGet, FacultateCreate, FacultateUpdate

router_facultati = APIRouter(
    prefix="/facultati",
    tags=["Facultati"]
)


def _map_facultate(db_facultate: Facultati) -> FacultateGet:
    return FacultateGet(
        id=db_facultate.id,
        nume_facultate=db_facultate.nume
    )


@router_facultati.get("/")
async def get_all_facultati() -> list[FacultateGet]:
    """
    Endpoint pentru obținerea tuturor facultăților.
    """
    facultati = get_all_facultati_from_db()
    return [_map_facultate(facultate) for facultate in facultati]


@router_facultati.get("/{facultate_id}")
async def get_facultate(facultate_id: uuid.UUID) -> FacultateGet:
    """
    Endpoint pentru obținerea unei facultăți după ID.
    """
    facultate = get_facultate_by_id(facultate_id)

    if facultate is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Facultate not found")

    return _map_facultate(facultate)


@router_facultati.post("/", status_code=status.HTTP_201_CREATED)
async def create_facultate(facultate: FacultateCreate):
    """
    Endpoint pentru crearea unei noi facultăți.
    """
    new_facultate = create_facultate_in_db(facultate)

    if not new_facultate:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Error creating the facultate")

    return _map_facultate(new_facultate)


@router_facultati.put("/{facultate_id}")
async def update_facultate(facultate_id: uuid.UUID, facultate: FacultateUpdate):
    """
    Endpoint pentru actualizarea unei facultăți existente.
    """
    success = update_facultate_in_db(facultate_id, facultate)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Facultate not found")

    return {"message": "Facultate updated successfully"}


@router_facultati.delete("/{facultate_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_facultate(facultate_id: uuid.UUID):
    """
    Endpoint pentru ștergerea unei facultăți existente.
    """
    success = delete_facultate_by_id(facultate_id)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Facultate not found")
