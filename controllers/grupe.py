import uuid

from fastapi import APIRouter, HTTPException, status

from database.models import Grupe
from repository.grupe import get_grupa_by_id, get_all_grupe_from_db, create_grupa_in_db, update_grupa_in_db, delete_grupa_by_id
from return_models.grupe import GrupeGet, GrupeCreate, GrupeUpdate

router_grupe = APIRouter(
    prefix="/grupe",
    tags=["Grupe"]
)


def _map_grupa(db_grupa: Grupe) -> GrupeGet:
    return GrupeGet(
        id=db_grupa.id,
        id_facultate=db_grupa.id_facultate,
        id_specializare=db_grupa.id_specializare,
        an=db_grupa.an,
        numar_grupa=db_grupa.numar_grupa,
        litera_semigrupa=db_grupa.litera_semigrupa
    )


@router_grupe.get("/")
async def get_all_grupe() -> list[GrupeGet]:
    """
    Endpoint pentru obținerea tuturor grupelor
    """
    grupe = get_all_grupe_from_db()
    return [_map_grupa(grupa) for grupa in grupe]


@router_grupe.get("/{grupa_id}")
async def get_grupa(grupa_id: uuid.UUID) -> GrupeGet:
    """
    Endpoint pentru obținerea unei grupe după ID
    """
    grupa = get_grupa_by_id(grupa_id)

    if grupa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Grupa not found")

    return _map_grupa(grupa)


@router_grupe.post("/", status_code=status.HTTP_201_CREATED)
async def create_grupa(grupa: GrupeCreate):
    """
    Endpoint pentru crearea unei noi grupe
    """
    new_grupa = create_grupa_in_db(grupa)

    if not new_grupa:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Error creating the grupe")

    return _map_grupa(new_grupa)


@router_grupe.put("/{grupa_id}")
async def update_grupa(grupa_id: uuid.UUID, grupa: GrupeUpdate):
    """
    Endpoint pentru actualizarea unei grupe existente
    """
    success = update_grupa_in_db(grupa_id, grupa)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Grupa not found")

    return {"message": "Grupa updated successfully"}


@router_grupe.delete("/{grupa_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_grupa(grupa_id: uuid.UUID):
    """
    Endpoint pentru ștergerea unei grupe existente
    """
    success = delete_grupa_by_id(grupa_id)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Grupa not found")
