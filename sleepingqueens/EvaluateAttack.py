from abc import ABC, abstractmethod

from sleepingqueens.AwokenQueenPosition import AwokenQueenPosition
from sleepingqueens.CardType import CardType
from sleepingqueens.GameState import GameState
from sleepingqueens.HandPosition import HandPosition
from sleepingqueens.MoveQueen import MoveQueen
from sleepingqueens.Position import Position


class EvaluateAttackInterface(ABC):
    @abstractmethod
    def attack(self, gamestate: GameState, defense: CardType, from_: AwokenQueenPosition,
               to: Position) -> None:
        pass


class EvaluateAttack(EvaluateAttackInterface):
    move: MoveQueen

    def attack(self, gamestate: GameState, defense: CardType, from_: AwokenQueenPosition,
               to: Position) -> None:
        handp = gamestate.players[from_.getPlayerIndex()].hand.hasCardOfType(defense)
        if isinstance(handp, HandPosition):
            gamestate.players[from_.getPlayerIndex()].hand.removePickedCardsAndRedraw(
                [handp])
        else:
            self.move.move(gamestate, from_, to)

    def __init__(self):
        self.move = MoveQueen()
