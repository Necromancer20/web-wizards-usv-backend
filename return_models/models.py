from pydantic import BaseModel


class Utilizator(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    rol: str


