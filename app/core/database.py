"""Configures the database engine, table creation, and database sessions."""

from collections.abc import Generator
from sqlmodel import Session, SQLModel, create_engine

# Import database models so SQLModel can register them in its metadata
# create_all() uses this metadata to know which tables to create
from app.models.trip import Trip

# SQLite database filename
sqlite_file_name = "travel.db"
# SQLAlchemy connection URL for the SQLite database
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Engine manages communication between Python (SQLModel) and SQLite
# echo=True prints SQL statements to the terminal
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables() -> None:
    # Create every registered SQLModel table if it doesnt already exist
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    # Open a database session for a request
    # FastAPI injects this session into routes that depend on it
    # Then automatically close it when the request has finished
    with Session(engine) as session:
        yield session
