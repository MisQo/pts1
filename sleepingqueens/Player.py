from typing import Optional

from sleepingqueens.Card import Card
from sleepingqueens.CardType import CardType
from sleepingqueens.Hand import Hand
from sleepingqueens.HandPosition import HandPosition
from sleepingqueens.PlayerState import PlayerState
from sleepingqueens.Position import Position


class Player:
    state: PlayerState
    hand: Hand

    def validDiscard(self, cards: list[Card]) -> bool:
        for c in cards:
            if c.type is not CardType.Number:
                return False

        if len(cards) == 2:
            return cards[0].value == cards[1].value

        return sum([c.value for c in cards[:-1]]) == cards[-1].value

    def play(self, cards: list[HandPosition], discard: bool, targetPlayer: Optional[Player] = None,
             targetQueen: Optional[Position] = None):
        if len(cards) == 0:
            raise Exception("no cards to play")

        if discard:
            if len(cards) == 1:
                self.hand.removePickedCardsAndRedraw(cards)
                return
            else:
                if not self.validDiscard(self.hand.pickCards(cards)):
                    raise Exception("invalid Discard turn")
                self.hand.removePickedCardsAndRedraw(cards)
                return

        card = self.hand.pickCards(cards)[0]

        if card.type == CardType.King:
            pass

        if card.type == CardType.Knight or card.type == CardType.SleepingPotion:
            pass

        raise Exception("invalid card played")

    def getPlayerState(self) -> PlayerState:
        return self.state
