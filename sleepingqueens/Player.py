from typing import Optional

from sleepingqueens.AwokenQueenPosition import AwokenQueenPosition
from sleepingqueens.CardType import CardType
from sleepingqueens.EvaluateAttack import EvaluateAttack, EvaluateAttackInterface
from sleepingqueens.EvaluateDiscard import EvaluateDiscard, EvaluateDiscardInterface
from sleepingqueens.GameState import GameState
from sleepingqueens.HandPosition import HandPosition
from sleepingqueens.MoveQueen import MoveQueen, MoveQueenInterface
from sleepingqueens.Position import Position
from sleepingqueens.SleepingQueenPosition import SleepingQueenPosition


class Player:
    playerIdx: int
    discard: EvaluateDiscardInterface
    move: MoveQueenInterface
    attack: EvaluateAttackInterface

    def play(self, gamestate: GameState, cards: list[HandPosition], discard: bool,
             targetQueen: Optional[Position] = None) -> None:
        if len(cards) == 0:
            raise Exception("no cards to play")

        if discard:
            if not self.discard.validDiscard(gamestate.players[self.playerIdx].hand.pickCards(cards)):
                raise Exception("invalid discard")
        else:
            if len(cards) > 1:
                raise Exception("multiple cards played")

        card = gamestate.players[self.playerIdx].hand.pickCards(cards)[0]

        if card.type.value == CardType.King.value:
            if not isinstance(targetQueen, SleepingQueenPosition):
                raise Exception("invalid target")
            newpos = 0
            while AwokenQueenPosition(newpos, self.playerIdx) in gamestate.awokenQueens:
                newpos += 1
            self.move.move(gamestate, targetQueen,
                           AwokenQueenPosition(newpos, self.playerIdx))

        if card.type.value == CardType.Knight.value:
            if not isinstance(targetQueen, AwokenQueenPosition):
                raise Exception("invalid target")
            newpos = 0
            while AwokenQueenPosition(newpos, self.playerIdx) in gamestate.awokenQueens:
                newpos += 1
            self.attack.attack(gamestate, CardType.Dragon, targetQueen, AwokenQueenPosition(newpos, self.playerIdx))

        if card.type.value == CardType.SleepingPotion.value:
            if not isinstance(targetQueen, AwokenQueenPosition):
                raise Exception("invalid target")
            newpos = 0
            while SleepingQueenPosition(newpos) in gamestate.sleepingQueens:
                newpos += 1
            self.attack.attack(gamestate, CardType.MagicWand, targetQueen, SleepingQueenPosition(newpos))

        if card.type.value == CardType.Dragon or card.type.value == CardType.MagicWand.value:
            raise Exception("invalid card played")

        gamestate.players[self.playerIdx].hand.removePickedCardsAndRedraw(cards)

    def __init__(self, id: int, _discard: EvaluateDiscardInterface = EvaluateDiscard(),
                 _move: MoveQueenInterface = MoveQueen(), _attack: EvaluateAttackInterface = EvaluateAttack()):
        self.playerIdx = id
        self.discard = _discard
        self.move = _move
        self.attack = _attack
