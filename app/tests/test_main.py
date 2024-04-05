from fastapi.testclient import TestClient
import json
from app.main import app 

client = TestClient(app)


def test_create_grocery_item():
    response = client.post(
        "/grocery/",
        json={
            "name": "Apple",
            "category": "Fruit",
            "quantity_in_stock": 20,
            "price_per_unit": 1.5,
            "supplier_name": "SupplierA",
            "contact_info": "suppliera@example.com"
        }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Apple"
    assert data["category"] == "Fruit"

def test_list_grocery():
    response = client.get("/grocery/")
    assert response.status_code == 200
    