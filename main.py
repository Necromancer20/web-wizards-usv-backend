import uuid

from fastapi import FastAPI

from database.models import UserRole
from return_models.models import Utilizator

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True})


@app.get("/test")
async def root() -> Utilizator:
    return Utilizator(
        id=str(uuid.uuid4()),
        first_name="Test First Name",
        last_name="Test Last Name",
        email="test@gmail.com",
        rol=UserRole.STUDENT,
    )
