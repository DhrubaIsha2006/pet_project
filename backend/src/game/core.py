from collections.abc import Callable
from dataclasses import dataclass

from src.game.constants import (
    COLUMNS,
    CONNECT,
    EMPTY,
    ROWS,
    WINNER,
)


def create_board():
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]


def validate_move(board, row, column):
    if row is None or column is None:
        return False

    if not (0 <= row < ROWS):
        return False

    if not (0 <= column < COLUMNS):
        return False

    if board[row][column] != EMPTY:
        return False

    if row == ROWS - 1:
        return True

    return board[row + 1][column] != EMPTY


@dataclass
class Direction:
    name: str
    condition: Callable[[int, int], bool]
    function: Callable[[list[list[int]], int, int, int], int]
    move_condition: Callable[[int, int, int], bool]
    move_row_col: Callable[[int, int, int], tuple[int, int]]


DIRECTIONS = [
    Direction(
        name="down",
        condition=lambda row, _: row <= ROWS - CONNECT,
        function=lambda board, row, col, i: board[row + i][col],
        move_condition=lambda row, col, i: row + i < ROWS,
        move_row_col=lambda row, col, i: (row + i, col),
    ),
    Direction(
        name="right",
        condition=lambda _, col: col <= COLUMNS - CONNECT,
        function=lambda board, row, col, i: board[row][col + i],
        move_condition=lambda row, col, i: col + i < COLUMNS,
        move_row_col=lambda row, col, i: (row, col + i),
    ),
    Direction(
        name="left down",
        condition=lambda row, col: row <= ROWS - CONNECT
        and col >= CONNECT - 1,
        function=lambda board, row, col, i: board[row + i][col - i],
        move_condition=lambda row, col, i: (row + i < ROWS and col - i >= 0),
        move_row_col=lambda row, col, i: (row + i, col - i),
    ),
    Direction(
        name="right down",
        condition=lambda row, col: (
            row <= ROWS - CONNECT and col <= COLUMNS - CONNECT
        ),
        function=lambda board, row, col, i: board[row + i][col + i],
        move_condition=lambda row, col, i: (
            row + i < ROWS and col + i < COLUMNS
        ),
        move_row_col=lambda row, col, i: (row + i, col + i),
    ),
]


def detect_winner(board):
    for row in range(ROWS):
        for column in range(COLUMNS):
            if board[row][column] == EMPTY:
                continue

            for direction in DIRECTIONS:
                if not direction.condition(row, column):
                    continue

                if all(
                    direction.function(board, row, column, i)
                    == board[row][column]
                    for i in range(CONNECT)
                ):
                    return board[row][column]

    return None


def mark_winner(board):
    for row in range(ROWS):
        for column in range(COLUMNS):
            if board[row][column] == EMPTY:
                continue

            for direction in DIRECTIONS:
                if not direction.condition(row, column):
                    continue

                if all(
                    direction.function(board, row, column, i)
                    == board[row][column]
                    for i in range(CONNECT)
                ):
                    for i in range(CONNECT):
                        winner_row, winner_column = direction.move_row_col(
                            row, column, i
                        )
                        board[winner_row][winner_column] = WINNER

                    return
