# Manage Products

This project enables efficient management of products through the following technologies:

- [FastAPI](https://fastapi.tiangolo.com): A powerful framework for building APIs with Python.
- SQLite: Default database with preloaded dummy data. Can be switched to PostgreSQL by setting `IS_POSTGRES_SET` to `True` in the `.env` file.
- [SQLModel](https://www.google.com/search?client=safari&rls=en&q=sql+tiangolo&ie=UTF-8&oe=UTF-8): Used for seamless interaction with the database.

## IMPORTANT

- Upon spinning up the server, a dummy superuser will be automatically created by the system.
- API documentation is accessible at [http://localhost:8000/docs](http://localhost:8000/docs)

## Getting Started
1. Install dependencies
    ```zsh
    # recommended to use virtual env
    pip install -r requirements.txt
    ```

2. Start FastAPI process
    ```zsh
    # Run the following command in the 'app' directory
    cd Product-Management
    uvicorn app.main:server --reload
    ```
    The FastAPI application will be accessible at [http://localhost:8000](http://localhost:8000).

3. Open local API docs & UI
    [http://localhost:8000/docs](http://localhost:8000/docs)

4. Run tests
    ```zsh
    # Run the following command in the 'app' directory
    pytest
    ```
    This will execute the tests using `pytest`.

Make sure to adjust the instructions based on the specific details of your project and the intended audience. Additionally, consider adding any other relevant information that might be helpful for someone setting up and running your FastAPI project.

## Run with Docker

Build the image.

```bash
docker build -t product-management .
```

Run a container using the image. Do not forget to have the environment
variables set in the `.env` file.

```bash
docker run -d --name product-management -p 8000:8000 --env-file .env --rm product-management
```

Now you can make all the same requests that were described in the previous
section, but to port `80`.

1. Open local API docs & UI
    [http://0.0.0.0/docs](http://0.0.0.0/docs)


You can see the logs of your container with `docker logs product-management` or
follow them adding the `-f` flag before the container name.
