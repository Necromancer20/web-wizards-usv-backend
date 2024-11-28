import uuid

from fastapi import APIRouter, HTTPException, status

from database.models import Utilizator
from repository.utilizatori import get_user_by_email, get_user_by_id, get_all_users_from_db, delete_user_by_id, \
    update_user_in_db, add_user_to_db
from return_models.utilizatori import UtilizatorLogin, UtilizatorGet, UtilizatorUpdate, UtilizatorCreate

router_utiliziatori = APIRouter(
    prefix="/utilizator",
    tags=["Utilizator"]
)


def _map_user(db_user: Utilizator) -> UtilizatorGet | UtilizatorLogin:
    return UtilizatorLogin(
        id=db_user.id,
        first_name=db_user.first_name,
        last_name=db_user.last_name,
        email=db_user.email,
        rol=db_user.rol
    )


@router_utiliziatori.post("/login")
async def login(email: str, parola: str) -> UtilizatorLogin:
    """
    Endpoint pentru autentificare.
    """
    utilizator = get_user_by_email(email)

    if utilizator is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The account doesn't exist.")

    result = _map_user(utilizator)

    if utilizator.password == parola:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid email or password.")


@router_utiliziatori.get("/")
async def get_all_users() -> list[UtilizatorGet]:
    """
    Endpoint pentru obținerea tuturor utilizatorilor
    """
    return [_map_user(utilizator) for utilizator in get_all_users_from_db()]


@router_utiliziatori.get("/{user_id}")
async def get_user(user_id: uuid.UUID) -> UtilizatorGet:
    """
    Endpoint pentru obținerea unui utilizator după ID
    """
    utilizator = get_user_by_id(user_id)

    if utilizator is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The account doesn't exist.")

    result = _map_user(utilizator)
    return result


@router_utiliziatori.put("/{user_id}")
async def update_user(user_id: uuid.UUID, user: UtilizatorUpdate):
    """
    Endpoint pentru actualizarea unui utilizator existent
    """
    success = update_user_in_db(user_id, user)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The account doesn't exist.")


@router_utiliziatori.delete("/{user_id}", status_code=200)
async def delete_user(user_id: uuid.UUID):
    """
    Endpoint pentru ștergerea unui utilizator existent
    """
    success = delete_user_by_id(user_id)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The account doesn't exist.")


@router_utiliziatori.post("/")
async def create_user(new_user: UtilizatorCreate) -> UtilizatorGet:
    """
    Endpoint pentru crearea unui utilizator nou
    """
    utilizator = add_user_to_db(new_user)
    return _map_user(utilizator)
