from functools import lru_cache
from fastapi import FastAPI
import uvicorn
from .config import Settings



app = FastAPI()
@lru_cache()
def get_settings():
    return Settings()



from .routers import pessoas

app.include_router(pessoas.router)

if __name__ == "__main__":
    uvicorn.run(app)