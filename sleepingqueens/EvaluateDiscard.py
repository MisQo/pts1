from abc import ABC, abstractmethod

from sleepingqueens.Card import Card
from sleepingqueens.CardType import CardType


class EvaluateDiscardInterface(ABC):
    @abstractmethod
    def validDiscard(self, cards: list[Card]) -> bool:
        pass


class EvaluateDiscard(EvaluateDiscardInterface):
    def validDiscard(self, cards: list[Card]) -> bool:
        if len(cards) == 1:
            return True

        if len(cards) == 2:
            return cards[0] == cards[1]

        for c in cards:
            if c.type.value is not CardType.Number.value:
                return False

        return sum([c.value for c in cards[:-1]]) == cards[-1].value
