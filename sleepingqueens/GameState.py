from dataclasses import dataclass
from typing import Optional

from sleepingqueens.Card import Card
from sleepingqueens.Queen import Queen


@dataclass
class GameState:
    numberOfPlayers: int
    onTurn: int
    sleepingQueens: set[sleepingQueenPosition]
    cards: dict[HandPosition, Optional[Card]]
    awokenQueens: dict[AwokenQueenPosition, Queen]
    cardsDiscardedLastTurn: list[Card]