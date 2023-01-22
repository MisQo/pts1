from dataclasses import dataclass
from typing import Optional
from sleepingqueens.Card import Card
from sleepingqueens.Queen import Queen


@dataclass
class PlayerState:
    cards: dict[int, Optional[Card]]
    awokenQueens: dict[int, Queen]
