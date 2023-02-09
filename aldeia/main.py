from fastapi import FastAPI

from .db import get_engine

app = FastAPI()
engine = get_engine()


from .routers import pessoas

app.include_router(pessoas.router)
