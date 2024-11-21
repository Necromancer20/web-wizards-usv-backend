from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from database.models import Utilizator


def verifica_credentiale(session: Session, email: str, parola: str) -> dict:
    """
    Verifică dacă combinația email și parolă este validă.

    :param session: O instanță SQLAlchemy Session.
    :param email: Email-ul utilizatorului.
    :param parola: Parola utilizatorului.
    :return: Un dicționar cu statusul autentificării.
    """
    try:
        # Caută utilizatorul în baza de date după email
        utilizator = session.query(Utilizator).filter(Utilizator.email == email).one()

        # Verifică dacă parola este corectă
        if utilizator.password == parola:
            return {"status": "success", "message": "Autentificare reușită."}
        else:
            return {"status": "error", "message": "Parola este incorectă."}

    except NoResultFound:
        return {"status": "error", "message": "Email-ul nu există în sistem."}
    except Exception as e:
        return {"status": "error", "message": f"Eroare internă: {str(e)}"}
