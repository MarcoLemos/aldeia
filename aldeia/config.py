from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    app_name: str = "aldeia"
    mongo_username: str
    mongo_password: str
    db_name: str

    class Config:
        env_file = os.path.expanduser(".env")
