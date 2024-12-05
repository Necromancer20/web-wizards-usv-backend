import enum

from sqlalchemy import VARCHAR, Integer, Boolean, DateTime, Enum, ForeignKey, Text
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


# Enums
class UserRole(enum.Enum):
    ADMIN = "admin"
    STUDENT = "student"
    PROFESSOR = "professor"


class ExamType(enum.Enum):
    EXAMEN = "examen"
    COLOCVIU = "colocviu"


class ExamStatus(enum.Enum):
    ACCEPTAT = "aceptat"
    REFUZAT = "refuzat"
    IN_ASTEPTARE = "in_asteptare"


# Tables

class Facultati(Base):
    __tablename__ = "facultati"

    id: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, primary_key=True)
    nume: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)


class Specializari(Base):
    __tablename__ = "specializari"

    id: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, primary_key=True)
    id_facultate: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, ForeignKey("facultati.id"), nullable=False)
    nume: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)


class Grupe(Base):
    __tablename__ = "grupe"

    id: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, primary_key=True)
    id_facultate: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, ForeignKey("facultati.id"), nullable=False)
    id_specializare: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, ForeignKey("specializari.id"), nullable=False)
    an: Mapped[int] = mapped_column(Integer, nullable=False)
    numar_grupa: Mapped[int] = mapped_column(Integer, nullable=False)
    litera_semigrupa: Mapped[int] = mapped_column(Integer, nullable=False)


class Materii(Base):
    __tablename__ = "materii"

    id: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, primary_key=True)
    id_grupa: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, ForeignKey("grupe.id"), nullable=False)
    id_profesor: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, ForeignKey("utilizator.id"),
                                             nullable=False)  # Assuming professor ID is a UUID
    semestrul: Mapped[int] = mapped_column(Integer, nullable=False)
    nume: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    nume_abreviat: Mapped[str] = mapped_column(VARCHAR(10), nullable=False)
    numar_credite: Mapped[int] = mapped_column(Integer, nullable=False)
    durata_examen_minute: Mapped[int] = mapped_column(Integer, nullable=False)


class ProgramariExamen(Base):
    __tablename__ = "programari_examen"

    id: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, primary_key=True)
    id_materie: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, ForeignKey("materii.id"), nullable=False)
    id_profesor: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, ForeignKey("utilizator.id"), nullable=False)
    id_student_creator: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, ForeignKey("utilizator.id"), nullable=False)
    id_grupa: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, ForeignKey("grupe.id"), nullable=False)
    data_examen: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    locatie: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    tip_examen: Mapped[ExamType] = mapped_column(Enum(ExamType), nullable=False)
    observatii: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[ExamStatus] = mapped_column(Enum(ExamStatus), nullable=False)


class Utilizator(Base):
    __tablename__ = "utilizator"

    id: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, primary_key=True)
    first_name: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    last_name: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    rol: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False)


class GrupeUtilizator(Base):
    __tablename__ = "grupe_utilizator"

    id_utilizator: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, ForeignKey("utilizator.id"), primary_key=True)
    id_grupa: Mapped[str] = mapped_column(UNIQUEIDENTIFIER, ForeignKey("grupe.id"), primary_key=True)
    este_sef_semigrupa: Mapped[bool] = mapped_column(Boolean, nullable=False)
