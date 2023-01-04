"""Database Settings."""

import os
from typing import Final, Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import Session, sessionmaker

# Load Environment Variables
load_dotenv()

# Reference Environment Variables
DB_HOST = str(os.getenv("DB_HOST"))
DB_PORT = str(os.getenv("DB_PORT"))
DB_NAME = str(os.getenv("DB_NAME"))
DB_USER = str(os.getenv("DB_USER"))
DB_PASSWORD = str(os.getenv("DB_PASSWORD"))

# Database URL
DATABASE_URL = "postgresql://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_HOST + ":" + DB_PORT + "/" + DB_NAME

# Database Engine
engine: Final[Engine] = create_engine(DATABASE_URL, echo=True)

# Database Session
SessionLocal: sessionmaker = sessionmaker(bind=engine)

# Base Model
Base: Final[DeclarativeMeta] = declarative_base()


# Database Access Utility
def get_db() -> Generator[Session, None, None]:
    """Get Database Session."""
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
