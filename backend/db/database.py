import os 
from dotenv import load_dotenv
load_dotenv()

#database imports 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

postgres_connection_string = os.getenv("POSTGRESQL_CONNECTION_STRING")

engine = create_engine("postgres_connection_string")

SessionLocal = sessionmaker(autoflush=False , autocommit = False , bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()