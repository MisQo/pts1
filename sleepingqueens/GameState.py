from dataclasses import dataclass

from sleepingqueens.AwokenQueenPosition import AwokenQueenPosition
from sleepingqueens.PlayerState import PlayerState
from sleepingqueens.Queen import Queen
from sleepingqueens.SleepingQueenPosition import SleepingQueenPosition


@dataclass
class GameState:
    numberOfPlayers: int
    onTurn: int
    sleepingQueens: dict[SleepingQueenPosition, Queen]
    awokenQueens: dict[AwokenQueenPosition, Queen]
    players: list[PlayerState]
