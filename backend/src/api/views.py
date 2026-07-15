import importlib

from fastapi import APIRouter

from src.api.models import Game, StartGame

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

    app = get_current_app()

    collection_name = "games"
    collection = app.state.mongodb.get_collection(collection_name)

    insert_result = await collection.insert_one(data)

    result = await collection.find_one({"_id": insert_result.inserted_id})

    return Game(**result)


def get_current_app():
    module = importlib.import_module("src.main")
    return getattr(module, "app")
