from fastapi.testclient import TestClient
import json
from app.main import server
from sqlmodel import Session
from app.tests.utils import create_random_product

client = TestClient(server)


def test_create_product(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
):
    response = client.post(
        "/products/",
        headers=superuser_token_headers,
        json={
            "product_name": "Asus2",
            "price": 60000,
            "quantity_in_stock": 20,
            "quantity": 5,
            "description": "New Model",
        },
    )
    print(response.text)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["product_name"] == "Asus2"
    assert data["price"] == 60000


def test_get_products(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
):
    response = client.get("/products/", headers=superuser_token_headers)
    assert response.status_code == 200


def test_read_products(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    products = create_random_product(db)
    response = client.get(
        f"/products/{products.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["product_name"] == products.product_name
    assert content["price"] == products.price
    assert content["quantity"] == products.quantity
    assert content["price"] == products.price
