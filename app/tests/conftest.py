from collections.abc import Generator
import pytest
from fastapi.testclient import TestClient
from app.tests.utils import get_superuser_token_headers
from app.main import server
from sqlmodel import Session, delete
from app.models.database import engine, init_db
from app.models.models  import Product, User



@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        init_db(session)
        yield session
        statement = delete(Product)
        session.execute(statement)
        statement = delete(User)
        session.execute(statement)
        session.commit()

@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(server) as c:
        yield c
        
        
        
@pytest.fixture(scope="module")
def superuser_token_headers(client: TestClient) -> dict[str, str]:
    return get_superuser_token_headers(client)
