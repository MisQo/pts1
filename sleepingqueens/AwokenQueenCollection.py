from typing import overload

from sleepingqueens.AwokenQueenPosition import AwokenQueenPosition
from sleepingqueens.Queen import Queen
from sleepingqueens.QueenCollection import QueenCollection


class AwokenQueenCollection(QueenCollection):
    playerIdx: int

    queens: dict[AwokenQueenPosition, Queen]

    def addQueen(self, queen: Queen):
        for i in range(len(self.queens) + 1):
            if AwokenQueenPosition(_cardIndex=i, _playerIndex=self.playerIdx) not in self.queens:
                self.queens[AwokenQueenPosition(_cardIndex=i, _playerIndex=self.playerIdx)] = queen
                return

    def removeQueen(self, position: AwokenQueenPosition):
        return self.queens.pop(position)
