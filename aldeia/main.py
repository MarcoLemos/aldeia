"""from pymongo import MongoClient
from odmantic import SyncEngine, Model

#from odmantic import SyncEngine, Model
uri='mongodb://root:example@localhost:27017/'
client = MongoClient(uri)
engine = SyncEngine(client=client, database="teste")

#database = client['teste']
#collection = database['pessoas']

class pessoas(Model):
    nome: str"""


from fastapi import FastAPI

from .db import get_engine

app = FastAPI()
engine = get_engine()


from .routers import pessoas

app.include_router(pessoas.router)


"""

@app.get("/", response_model=List[Pessoas])
async def get_pessoas():
    pessoas = await engine.find(Pessoas)
    return pessoas


@app.get("/pessoas/count", response_model=int)
async def count_pessoas():
    count = await engine.count(Pessoas)
    return count


@app.get("/pessoas/{id}", response_model=Pessoas)
async def get_pessoa_by_id(id: ObjectId):
    pessoa = await engine.find_one(Pessoas, Pessoas.id == id)
    if pessoa is None:
        raise HTTPException(404)
    return pessoa"""
