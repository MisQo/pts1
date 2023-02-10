from dataclasses import dataclass
from sleepingqueens.CardType import CardType


@dataclass
class Card:
    type: CardType
    value: int

    def __init__(self, cardtype: CardType, value_: int = 0):
        self.type = cardtype
        self.value = value_

    def __hash__(self):
        return hash((self.type, self.value))
