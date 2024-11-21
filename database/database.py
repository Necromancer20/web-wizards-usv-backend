from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL-ul către baza de date
DATABASE_URL = "mssql+pyodbc://web-wiz-dev-acc:tfNoWcopU3KN3ehdPzWl@sql-web-wizards-dev-gwc.database.windows.net/sqldb-web-wizards-dev-gwc?driver=ODBC+Driver+17+for+SQL+Server"

# Creează engine-ul pentru baza de date
engine = create_engine(DATABASE_URL)

# Creează sesiuni SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
