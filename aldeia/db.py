from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from .main import get_settings

usr = get_settings().mongo_username
passw = get_settings().mongo_password
uri = f'mongodb://{usr}:{passw}@localhost:27017/admin'
client = AsyncIOMotorClient(uri)
engine = AIOEngine(client=client, database='teste')

