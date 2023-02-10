from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine



uri = 'mongodb://root:exemple@localhost:27017/admin'
client = AsyncIOMotorClient(uri)
engine = AIOEngine(client=client, database='teste')

