from fastapi import FastAPI
from app.models.database import init_db
from app.api.main import api_router
from sqlmodel import Session
from app.models.database import engine
from app.core.config import settings
from app.logger import configure_logs

# Configure logs to appear in the terminal.
configure_logs()

description = """
This system helps you manage products. 🚀

## Products

You can perform CRUD operations on products. 
For all operations, the user must be authorized.
Delete and create user functionalities are only performed by superusers.

## Authenticate

You can log in to the system using the 'Authorize' button by providing your username and password.
Only a username and password are required.

## For Demo Purposes

You can use the below superuser credentials for demonstration:

* **Username: admin@example.com**.
* **Password: test@pass**.

"""




server = FastAPI(
    title=settings.PROJECT_NAME,
    description=description

)


@server.on_event("startup")
def on_startup():
    with Session(engine) as session:
        init_db(session)


server.include_router(api_router)
