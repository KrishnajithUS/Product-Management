from fastapi import APIRouter, HTTPException, Depends
from app.models.models import Product, ProductCreate, ProductRead, ProductUpdate
from app.api.deps import SessionDep
from typing import List
from app.service import products


router = APIRouter()


@router.get("/products/", tags=["products"], response_model=List[ProductRead])
def get_products(session: SessionDep):
    product_list = products.get_products(session = session)
    return product_list


@router.post("/products/", tags=["products"], response_model=ProductRead)
def create_product(product_in: ProductCreate, session: SessionDep):
    product = products.get_product_by_name(session=session, name=product_in.product_name)
    if product:
        raise HTTPException(
            status_code=400,
            detail="The product with this name already exists in the system.",
        )
        
    product = products.create_product(session=session, product_create=product_in)
    return product


@router.put("/products/{id}", tags=["products"], response_model=ProductRead)
def update_product(product_in: ProductUpdate, session: SessionDep, id:int):
    product = session.get(Product, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product = products.update_product(session=session, product_update=product_in,
                                      product=product,id=id)
    return product


@router.delete("/products/{id}", tags=["products"])
def delete_product(session: SessionDep, id:int):
    product = session.get(Product, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    session.delete(product)
    session.commit()
    return {"ok": True}