from sleepingqueens.Card import Card
import random


class DrawingAndDiscardPile:
    drawPile: list[Card]
    discardPile: list[Card]

    seed: int

    def setSeed(self, _seed: int) -> None:
        self.seed = _seed
        random.seed(self.seed)

    ### TODO strategy

    def discardAndDraw(self, cards: list[Card]) -> list[Card]:
        if len(self.drawPile) < len(cards):
            random.shuffle(self.discardPile)
            self.drawPile += self.discardPile
            self.discardPile = cards
        else:
            self.discardPile += cards

        return [self.drawPile.pop(0) for _ in range(len(cards))]

    def __init__(self, draw: list[Card], discard: list[Card] = [], _seed: int = 0):
        self.drawPile = draw
        self.discardPile = discard
        self.setSeed(_seed)

    def getDrawPile(self) -> list[Card]:
        return self.drawPile

    def getDiscardPile(self) -> list[Card]:
        return self.discardPile
