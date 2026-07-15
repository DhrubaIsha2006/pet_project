from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.configs.settings import settings


def get_mongodb() -> AsyncIOMotorDatabase:
    """Get MongoDB database instance."""

    client = AsyncIOMotorClient(settings.MONGO_DB_URL)
    return client.get_database(settings.MONGO_DB_DB)
