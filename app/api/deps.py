from collections.abc import Generator
from typing import Annotated
from sqlmodel import Session
from app.models.database import engine
from fastapi import Depends

# creating a session of db
def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
        
        
SessionDep = Annotated[Session, Depends(get_db)]
