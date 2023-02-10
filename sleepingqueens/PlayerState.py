from dataclasses import dataclass

from sleepingqueens.Hand import Hand


@dataclass
class PlayerState:
    playerIdx: int
    hand: Hand
