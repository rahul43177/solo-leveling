import os 
from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

postgres_connection_string = os.getenv("POSTGRESQL_CONNECTION_STRING")
if not postgres_connection_string:
    raise ValueError("POSTGRESQL_CONNECTION_STRING environment variable not set")

engine = create_engine(postgres_connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
