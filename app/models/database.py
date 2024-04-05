from sqlmodel import Session, create_engine, SQLModel


SQLITE_FILE_NAME = "sql_app.db"

SQLALCHEMY_DATABASE_URL = F"sqlite:///{SQLITE_FILE_NAME}/"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


def init_db() -> None:
    """Create Table Structure on Db"""
    SQLModel.metadata.create_all(engine)