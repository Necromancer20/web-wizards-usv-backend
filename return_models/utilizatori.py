from uuid import UUID
from pydantic import BaseModel, EmailStr, Field, validator

import enum


# Enums from database
class UserRole(enum.Enum):
    ADMIN = "admin"
    STUDENT = "student"
    PROFESSOR = "professor"


class UtilizatorLogin(BaseModel):
    id: UUID
    first_name: str = Field(..., min_length=2, max_length=100, description="Prenumele trebuie să aibă între 2 și 100 de caractere.")
    last_name: str = Field(..., min_length=2, max_length=100, description="Numele de familie trebuie să aibă între 2 și 100 de caractere.")
    email: EmailStr
    rol: UserRole

    @validator("first_name", "last_name")
    def validate_names(cls, value: str):
        if not value.isalpha():
            raise ValueError("Numele trebuie să conțină doar litere.")
        return value


class UtilizatorGet(UtilizatorLogin):
    pass


class UtilizatorUpdate(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=100, description="Prenumele trebuie să aibă între 2 și 100 de caractere.")
    last_name: str = Field(..., min_length=2, max_length=100, description="Numele de familie trebuie să aibă între 2 și 100 de caractere.")
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100, description="Parola trebuie să aibă între 8 și 100 de caractere.")
    rol: UserRole

    @validator("first_name", "last_name")
    def validate_names(cls, value: str):
        if not value.isalpha():
            raise ValueError("Numele trebuie să conțină doar litere.")
        return value

    @validator("password")
    def validate_password(cls, value: str):
        if not any(char.isdigit() for char in value):
            raise ValueError("Parola trebuie să conțină cel puțin un număr.")
        if not any(char.isupper() for char in value):
            raise ValueError("Parola trebuie să conțină cel puțin o literă mare.")
        if not any(char.islower() for char in value):
            raise ValueError("Parola trebuie să conțină cel puțin o literă mică.")
        return value


class UtilizatorCreate(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=100, description="Prenumele trebuie să aibă între 2 și 100 de caractere.")
    last_name: str = Field(..., min_length=2, max_length=100, description="Numele de familie trebuie să aibă între 2 și 100 de caractere.")
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100, description="Parola trebuie să aibă între 8 și 100 de caractere.")
    rol: UserRole

    @validator("first_name", "last_name")
    def validate_names(cls, value: str):
        if not value.isalpha():
            raise ValueError("Numele trebuie să conțină doar litere.")
        return value

    @validator("password")
    def validate_password(cls, value: str):
        if not any(char.isdigit() for char in value):
            raise ValueError("Parola trebuie să conțină cel puțin un număr.")
        if not any(char.isupper() for char in value):
            raise ValueError("Parola trebuie să conțină cel puțin o literă mare.")
        if not any(char.islower() for char in value):
            raise ValueError("Parola trebuie să conțină cel puțin o literă mică.")
        return value
