from app.core.config import settings
from fastapi.testclient import TestClient
from sqlmodel import Session
from app.models.models import Product, ProductCreate
from app.service import products
import random
import string


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def get_superuser_token_headers(client: TestClient) -> dict[str, str]:
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers


def create_random_product(db: Session) -> Product:
    product_name = random_lower_string()
    description = random_lower_string()
    quantity = 1
    price = 5500
    product_in = ProductCreate(product_name=product_name, description=description, quantity=quantity, price=price)
    print('productin__',product_in)
    return products.create_product(session=db, product_create=product_in)