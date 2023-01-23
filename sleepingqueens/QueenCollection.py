from sleepingqueens.Position import Position
from sleepingqueens.Queen import Queen


class QueenCollection:
    queens: dict[Position, Queen]

    def getQueens(self) -> dict[Position, Queen]:
        return self.queens

    def addQueen(self, queen: Queen):
        for i in range(len(self.queens) + 1):
            if Position(i) not in self.queens:
                self.queens[Position(i)] = queen
                return

    def removeQueen(self, position: Position):
        return self.queens.pop(position)
