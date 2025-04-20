import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker

load_dotenv()
postgres_string_connection = os.getenv("POSTGRESQL_CONNECTION_STRING")
engine = create_engine(postgres_string_connection)



