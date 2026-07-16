import importlib
from typing import Any, cast

from fastapi import FastAPI
from motor.motor_asyncio import (
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)
from pymongo.results import InsertOneResult

from src.api.models import MongoDBModel


class MongoDBClient:
    __instance = None
    mongodb: AsyncIOMotorDatabase

    def __new__(cls) -> "MongoDBClient":
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            app = get_current_app()
            cls.__instance.mongodb = app.state.mongodb

        return cls.__instance

    def get_collection(
        self,
        model: type[MongoDBModel],
    ) -> AsyncIOMotorCollection:
        collection_name = model.get_collection_name()
        return self.mongodb.get_collection(collection_name)

    async def insert(
        self,
        model: type[MongoDBModel],
        data: dict[str, Any],
    ) -> InsertOneResult:
        collection = self.get_collection(model)
        return await collection.insert_one(data)

    async def get(
        self,
        model: type[MongoDBModel],
        id: Any,
    ) -> dict[str, Any]:
        collection = self.get_collection(model)

        result = cast(
            dict[str, Any],
            await collection.find_one({"_id": id}),
        )

        return result | {"id": result.pop("_id")}


def get_current_app() -> FastAPI:
    module = importlib.import_module("src.main")
    return cast(FastAPI, getattr(module, "app"))
