from dataclasses import dataclass
from typing import Optional
from sleepingqueens.AwokenQueenPosition import AwokenQueenPosition
from sleepingqueens.Card import Card
from sleepingqueens.HandPosition import HandPosition
from sleepingqueens.Queen import Queen
from sleepingqueens.SleepingQueenPosition import SleepingQueenPosition


@dataclass
class GameState:
    numberOfPlayers: int
    onTurn: int
    sleepingQueens: set[SleepingQueenPosition]
    cards: dict[HandPosition, Optional[Card]]
    awokenQueens: dict[AwokenQueenPosition, Queen]
    cardsDiscardedLastTurn: list[Card]