from copy import copy
from typing import Optional
from sleepingqueens.Card import Card
from sleepingqueens.CardType import CardType
from sleepingqueens.DrawingAndDiscardPile import DrawingAndDiscardPile
from sleepingqueens.HandPosition import HandPosition


class Hand:
    playerIdx: int
    cards: dict[HandPosition, Card]
    deck: DrawingAndDiscardPile

    def pickCards(self, positions: list[HandPosition]) -> list[Card]:
        return [self.cards[x] for x in positions]

    def removePickedCardsAndRedraw(self, positions: list[HandPosition]) -> None:
        drawn = self.deck.discardAndDraw([self.cards[x] for x in positions])
        for i in range(len(drawn)):
            self.cards[positions[i]] = drawn[i]

    def hasCardOfType(self, type_: CardType) -> Optional[HandPosition]:
        for hp, c in self.cards.items():
            if c.type.value == type_.value:
                return hp
        return None

    def __init__(self, playeridx: int, _cards: dict[HandPosition, Card], _deck: DrawingAndDiscardPile):
        self.playerIdx = playeridx
        self.cards = copy(_cards)
        self.deck = copy(_deck)

    def getCards(self) -> dict[HandPosition, Card]:
        return copy(self.cards)
