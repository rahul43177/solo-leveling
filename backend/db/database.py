import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables from .env file
load_dotenv()

# Retrieve the PostgreSQL connection string from environment variables
DATABASE_STRING = os.getenv("POSTGRESQL_CONNECTION_STRING")

# Validate that the connection string is not None
if not DATABASE_STRING:
    raise ValueError("POSTGRESQL_CONNECTION_STRING environment variable is not set.")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_STRING)

# Create a session factory
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Create a base class for declarative ORM models
Base = declarative_base()

# Dependency to provide a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()