from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field

from src.api.fields import PyObjectId


class MongoDBModel(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    id: PyObjectId | None = Field(default=None)

    class Meta:
        collection_name: ClassVar[str]

    @classmethod
    def get_collection_name(cls) -> str:
        return cls.Meta.collection_name


class StartGame(BaseModel):
    player: str


class Game(MongoDBModel):
    class Meta:
        collection_name = "games"

    player1: str
    player2: str
