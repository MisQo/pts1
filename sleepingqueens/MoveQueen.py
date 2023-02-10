from typing import Optional

from sleepingqueens.AwokenQueenPosition import AwokenQueenPosition
from sleepingqueens.GameState import GameState
from sleepingqueens.Position import Position
from sleepingqueens.SleepingQueenPosition import SleepingQueenPosition


class MoveQueen:
    def move(self, gamestate: GameState, from_: Optional[Position], to: Position) -> None:

        if isinstance(from_, SleepingQueenPosition):
            if from_ not in gamestate.sleepingQueens:
                raise Exception("invalid queen position")
            queen = gamestate.sleepingQueens[from_]
            gamestate.sleepingQueens.pop(from_)
        elif isinstance(from_, AwokenQueenPosition):
            if from_ not in gamestate.awokenQueens:
                raise Exception("invalid queen position")
            queen = gamestate.awokenQueens[from_]
            gamestate.awokenQueens.pop(from_)
        else:
            raise Exception("invalid queen position")

        if isinstance(to, SleepingQueenPosition):
            if to in gamestate.sleepingQueens:
                raise Exception("invalid queen position")
            gamestate.sleepingQueens[to] = queen
        elif isinstance(to, AwokenQueenPosition):
            if to in gamestate.awokenQueens:
                raise Exception("invalid queen position")
            gamestate.awokenQueens[to] = queen
        else:
            raise Exception("invalid queen position")
