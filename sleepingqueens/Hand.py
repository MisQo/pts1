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

    def removePickedCardsAndRedraw(self, positions: list[HandPosition]) -> list[Card]:
        return self.deck.discardAndDraw([self.cards[x] for x in positions])

    def hasCardOfType(self, type: CardType) -> Optional[HandPosition]:
        for c in self.cards:
            if self.cards[c] == type:
                return c
        return None
