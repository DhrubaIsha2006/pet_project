from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from src.api.views import router as api_router
from src.configs.settings import settings
from src.db.mongo import get_mongodb_client


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup
    client = get_mongodb_client()
    db = client.get_database(settings.MONGO_DB_DB)

    app.mongodb = db  # type: ignore[attr-defined]

    yield

    # Shutdown
    client.close()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "pet project world"}
