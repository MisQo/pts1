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
        random.shuffle(self.discardPile)
        self.drawPile += self.discardPile
        self.discardPile = cards
        return [self.drawPile.pop(0) for _ in range(len(cards))]
