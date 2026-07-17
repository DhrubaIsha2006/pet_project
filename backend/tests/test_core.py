import pytest

from src.game.constants import EMPTY, PLAYER_ONE, PLAYER_TWO
from src.game.core import detect_winner, mark_winner, validate_move


@pytest.mark.parametrize(
    "row,column,expected",
    [
        (5, 3, True),
        (4, 3, False),
        (6, 3, False),
        (-1, 3, False),
        (3, 7, False),
        (3, -1, False),
        (None, 3, False),
        (3, None, False),
    ],
)
def test_validate_move(row, column, expected):
    board = [[EMPTY] * 7 for _ in range(6)]
    assert validate_move(board, row, column) is expected


@pytest.mark.parametrize(
    "board,expected",
    [
        (
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0],
                [0, 2, 1, 0, 0, 0, 0],
                [0, 2, 1, 0, 0, 0, 0],
                [0, 2, 1, 0, 0, 0, 0],
            ],
            PLAYER_ONE,
        ),
        (
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [2, 2, 0, 0, 0, 0, 0],
                [2, 2, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0],
            ],
            PLAYER_ONE,
        ),
        (
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 2, 0, 0, 0],
                [0, 1, 2, 2, 0, 0, 0],
                [1, 2, 2, 1, 0, 0, 0],
            ],
            PLAYER_ONE,
        ),
        (
            [
                [0, 0, 0, 0, 0, 0, 0],
                [2, 0, 0, 0, 0, 0, 0],
                [1, 2, 0, 0, 0, 0, 0],
                [2, 1, 2, 0, 0, 0, 0],
                [1, 2, 1, 2, 0, 0, 0],
                [2, 1, 1, 1, 2, 0, 0],
            ],
            PLAYER_TWO,
        ),
        (
            [[0] * 7 for _ in range(6)],
            None,
        ),
    ],
)
def test_detect_winner(board, expected):
    assert detect_winner(board) == expected


@pytest.mark.parametrize(
    "board,expected",
    [
        (
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0],
                [0, 2, 1, 0, 0, 0, 0],
                [0, 2, 1, 0, 0, 0, 0],
                [0, 2, 1, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 3, 0, 0, 0, 0],
                [0, 2, 3, 0, 0, 0, 0],
                [0, 2, 3, 0, 0, 0, 0],
                [0, 2, 3, 0, 0, 0, 0],
            ],
        ),
        (
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [2, 2, 0, 0, 0, 0, 0],
                [2, 2, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [2, 2, 0, 0, 0, 0, 0],
                [2, 2, 0, 0, 0, 0, 0],
                [3, 3, 3, 3, 0, 0, 0],
            ],
        ),
    ],
)
def test_mark_winner(board, expected):
    mark_winner(board)
    assert board == expected
