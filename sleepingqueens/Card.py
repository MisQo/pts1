from dataclasses import dataclass
from sleepingqueens.CardType import CardType


@dataclass
class Card:
    type: CardType
    value: int
