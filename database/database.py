import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv(".env")

SERVER_HOST = os.environ.get("SERVER_HOST")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DB_USERNAME = os.environ.get("DB_USERNAME")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

DATABASE_URL = f"mssql+pyodbc://{DB_USERNAME}:{DATABASE_PASSWORD}@{SERVER_HOST}/{DATABASE_NAME}?driver=ODBC+Driver+17+for+SQL+Server"

DATABASE_ENGINE = create_engine(DATABASE_URL)
