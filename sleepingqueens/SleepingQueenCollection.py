from typing import overload

from sleepingqueens.Queen import Queen
from sleepingqueens.QueenCollection import QueenCollection
from sleepingqueens.SleepingQueenPosition import SleepingQueenPosition


class SleepingQueenCollection(QueenCollection):
    queens: dict[SleepingQueenPosition, Queen]

    def addQueen(self, queen: Queen):
        for i in range(len(self.queens) + 1):
            if SleepingQueenPosition(i) not in self.queens:
                self.queens[SleepingQueenPosition(i)] = queen
                return

    def removeQueen(self, position: SleepingQueenPosition):
        return self.queens.pop(position)
