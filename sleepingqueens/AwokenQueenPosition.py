from dataclasses import dataclass
from sleepingqueens.Position import Position


@dataclass
class AwokenQueenPosition(Position):
    _playerIndex: int

    def getPlayerIndex(self) -> int:
        return self._playerIndex
