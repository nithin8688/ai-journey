from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/ai_journey1"

# Engines - manages connections to PostgreSQL
engine = create_engine(DATABASE_URL)

# SessionLocal - factory that creates new sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base - parent class for all ORM models
Base = declarative_base()