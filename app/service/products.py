from sqlmodel import Session, select
from app.models.models import Product, ProductCreate, ProductUpdate

# Product Table Related Operations


def create_product(session: Session, product_create: ProductCreate):
    db_product = Product.model_validate(product_create)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


def get_product_by_name(session: Session, name: str) -> Product | None:
    statement = select(Product).where(Product.product_name == name)
    product_instance = session.exec(statement).first()
    return product_instance


def get_products(session: Session, limit: int, skip: int) -> Product | None:
    statement = select(Product).offset(skip).limit(limit)
    products = session.exec(statement).all()
    return products


def update_product(
    session: Session, id: int, product_update: ProductUpdate, product: Product
) -> Product | None:
    product_data = product_update.model_dump(exclude_unset=True)
    product.sqlmodel_update(product_data)
    session.add(product)
    session.commit()
    session.refresh(product)
    return product
