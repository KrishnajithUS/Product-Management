from sqlmodel import Session, create_engine, SQLModel, select
from app.core.config import settings
from app.models.models import UserCreate, User
from app.service import users

import logging

SQLITE_FILE_NAME = "sql_app.db"

if settings.IS_POSTGRES_SET:
    SQLALCHEMY_DATABASE_URL = str(settings.SQLALCHEMY_DATABASE_URI)
else:
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{SQLITE_FILE_NAME}/"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


def init_db(session: Session) -> None:
    """Create Table Structure on Db"""
    SQLModel.metadata.create_all(engine)

    # create a super user for testing if doesn't exist
    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        logging.info(f"creating new super user with email {settings.FIRST_SUPERUSER}")
        user = users.create_user(session=session, user_create=user_in)
        if user:
            logging.info("User creation successfully")
