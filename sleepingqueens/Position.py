from dataclasses import dataclass


@dataclass
class Position:
    _cardIndex: int

    def getCardIndex(self) -> int:
        return self._cardIndex
