from abc import ABC, abstractmethod

from sleepingqueens.Card import Card
import random
from copy import copy


class Strategy(ABC):
    @abstractmethod
    def handleShuffling(self, draw: list[Card], discard: list[Card], cards: list[Card]) -> None:
        pass


class ConcreteStrategyA(Strategy):
    # player CANT draw just discarded cards
    def handleShuffling(self, draw: list[Card], discard: list[Card], cards: list[Card]) -> None:
        random.shuffle(discard)
        draw += discard
        while len(discard) > 0:
            discard.pop()
        discard += cards


class ConcreteStrategyB(Strategy):
    # player CAN draw just discarded cards
    def handleShuffling(self, draw: list[Card], discard: list[Card], cards: list[Card]) -> None:
        discard += cards
        random.shuffle(discard)
        draw += discard


class DrawingAndDiscardPile:
    drawPile: list[Card]
    discardPile: list[Card]
    strategy: Strategy
    seed: int

    def setSeed(self, _seed: int) -> None:
        self.seed = _seed
        random.seed(self.seed)

    def discardAndDraw(self, cards: list[Card]) -> list[Card]:
        if len(self.drawPile) < len(cards):
            self.strategy.handleShuffling(self.drawPile, self.discardPile, cards)
        else:
            self.discardPile += cards

        return [self.drawPile.pop(0) for _ in range(len(cards))]

    def __init__(self, draw: list[Card], discard: list[Card] = [], _seed: int = 0,
                 _strategy: Strategy = ConcreteStrategyA()):
        self.drawPile = draw
        self.discardPile = discard
        self.setSeed(_seed)
        self.strategy = _strategy

    def getDrawPile(self) -> list[Card]:
        return copy(self.drawPile)

    def getDiscardPile(self) -> list[Card]:
        return copy(self.discardPile)
