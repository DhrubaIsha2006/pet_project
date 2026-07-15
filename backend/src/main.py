from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.views import router
from src.db.mongo import get_mongodb


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    mongodb = get_mongodb()
    app.state.mongodb = mongodb

    yield

    # shutdown
    app.state.mongodb.client.close()


app = FastAPI(lifespan=lifespan)
app.include_router(router)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "pet project world"}
