from sqlmodel import Session, create_engine, SQLModel
from app.core.config import settings

SQLITE_FILE_NAME = "sql_app.db"

if settings.IS_POSTGRES_SET:
    SQLALCHEMY_DATABASE_URL = str(settings.SQLALCHEMY_DATABASE_URI)
else:
    SQLALCHEMY_DATABASE_URL = F"sqlite:///{SQLITE_FILE_NAME}/"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


def init_db() -> None:
    """Create Table Structure on Db"""
    SQLModel.metadata.create_all(engine)