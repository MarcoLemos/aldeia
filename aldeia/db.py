from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine


def get_engine():
    uri = 'mongodb://root:example@localhost:27017/'
    client = AsyncIOMotorClient(uri)
    engine = AIOEngine(client=client, database='teste')
    return engine
