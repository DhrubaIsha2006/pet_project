from motor.motor_asyncio import AsyncIOMotorClient

from src.configs.settings import settings


def get_mongodb_client() -> AsyncIOMotorClient:
    """Get MongoDB client instance."""
    return AsyncIOMotorClient(settings.MONGO_DB_URL)
