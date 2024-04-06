from sqlmodel import Field, SQLModel, Relationship


class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Manual Thomas Adeshina",
                "email": "testtest@x.com",
                "password": "weakpassword",
            }
        }


# Properties to return via API, id is always required
class UserOut(UserBase):
    id: int


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str


class ProductBase(SQLModel):
    product_name: str = Field(unique=True)
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


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: int | None = None
