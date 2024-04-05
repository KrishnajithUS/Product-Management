from sqlmodel import Field, SQLModel

class ProductBase(SQLModel):
    product_name: str = Field(unique = True)  
    price: float
    quantity: int 
    description: str | None = Field(default=None)  


class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)



class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int


class ProductUpdate(ProductBase):
    product_name: str | None = None
    price: float | None = None
    quantity: int | None = None
    description: str | None = None