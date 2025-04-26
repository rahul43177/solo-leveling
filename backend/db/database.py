import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

load_dotenv()

postgres_connection_string = os.getenv("POSTGRESQL_CONNECTION_STRING")

engine = create_engine(postgres_connection_string)

SessionLocal = sessionmaker(autocommit = False , autoflush= False , bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try :
        yield db 
    finally:
        db.close()


