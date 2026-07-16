from fastapi import APIRouter

from src.api.models import Game, StartGame
from src.db.client import MongoDBClient

router = APIRouter(
    prefix="/games",
    tags=["Games"],
)


@router.post("/")
async def start_new_game(player_data: StartGame) -> Game:
    data = {
        "player1": player_data.player,
        "player2": player_data.player,
    }

    client = MongoDBClient()

    insert_result = await client.insert(Game, data)

    result = await client.get(Game, insert_result.inserted_id)

    return Game(**result)
