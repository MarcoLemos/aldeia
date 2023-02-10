from fastapi import FastAPI
from . import db

app = FastAPI()
engine = db.engine


from .routers import pessoas

app.include_router(pessoas.router)
