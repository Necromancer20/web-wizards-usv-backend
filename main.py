import uuid

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.models import UserRole
from return_models.models import Utilizator
from backend.auth_service import verifica_credentiale
from database.database import SessionLocal  # Asigură-te că ai configurat o sesiune SQLAlchemy

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True})

# Dependency pentru sesiunea DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/test")
async def root() -> Utilizator:
    return Utilizator(
        id=str(uuid.uuid4()),
        first_name="Test First Name",
        last_name="Test Last Name",
        email="test@gmail.com",
        rol=UserRole.STUDENT,
    )

@app.post("/login")
async def login(email: str, parola: str, db: Session = Depends(get_db)):
    """
    Endpoint pentru autentificare.
    """
    rezultat = verifica_credentiale(db, email, parola)
    if rezultat["status"] == "success":
        return {"message": rezultat["message"]}
    raise HTTPException(status_code=401, detail=rezultat["message"])

@app.get("/materii")
async def root() -> Utilizator:
    return []
