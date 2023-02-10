from typing import Optional

from sleepingqueens.AwokenQueenPosition import AwokenQueenPosition
from sleepingqueens.CardType import CardType
from sleepingqueens.EvaluateAttack import EvaluateAttack
from sleepingqueens.EvaluateDiscard import EvaluateDiscard
from sleepingqueens.GameState import GameState
from sleepingqueens.HandPosition import HandPosition
from sleepingqueens.MoveQueen import MoveQueen
from sleepingqueens.Position import Position


class Player:
    playerIdx: int
    discard: EvaluateDiscard
    move: MoveQueen
    attack: EvaluateAttack

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
            newpos = 0
            while AwokenQueenPosition(newpos, self.playerIdx) in gamestate.awokenQueens:
                newpos += 1
            self.move.move(gamestate, targetQueen,
                           AwokenQueenPosition(newpos, self.playerIdx))

        if card.type.value == CardType.Knight.value or card.type.value == CardType.SleepingPotion.value:
            if not isinstance(targetQueen, AwokenQueenPosition):
                raise Exception("invalid target")
            newpos = 0
            while AwokenQueenPosition(newpos, self.playerIdx) in gamestate.awokenQueens:
                newpos += 1
            self.attack.attack(gamestate,
                               CardType.Dragon if card.type.value == CardType.Knight.value else CardType.MagicWand,
                               targetQueen, AwokenQueenPosition(newpos, self.playerIdx))

        if card.type.value == CardType.Dragon or card.type.value == CardType.MagicWand.value:
            raise Exception("invalid card played")

        gamestate.players[self.playerIdx].hand.removePickedCardsAndRedraw(cards)

    def __init__(self, id: int):
        self.playerIdx = id
        self.discard = EvaluateDiscard()
        self.move = MoveQueen()
        self.attack = EvaluateAttack()
