from sleepingqueens.AwokenQueenPosition import AwokenQueenPosition
from sleepingqueens.CardType import CardType
from sleepingqueens.GameState import GameState
from sleepingqueens.HandPosition import HandPosition
from sleepingqueens.MoveQueen import MoveQueen


class EvaluateAttack:
    move: MoveQueen

    def attack(self, gamestate: GameState, defense: CardType, from_: AwokenQueenPosition,
               to: AwokenQueenPosition) -> None:
        handp = gamestate.players[from_.getPlayerIndex()].hand.hasCardOfType(defense)
        if isinstance(handp, HandPosition):
            gamestate.players[from_.getPlayerIndex()].hand.removePickedCardsAndRedraw(
                [handp])
        else:
            self.move.move(gamestate, from_, to)

    def __init__(self):
        self.move = MoveQueen()
