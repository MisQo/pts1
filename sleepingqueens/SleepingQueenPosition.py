from dataclasses import dataclass
from sleepingqueens.Position import Position


@dataclass
class SleepingQueenPosition(Position):
    def __hash__(self):
        return hash(self._cardIndex)
