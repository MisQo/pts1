from unittest import TestCase

from sleepingqueens.CardType import CardType
from sleepingqueens.Card import Card
from sleepingqueens.Player import EvaluateDiscard


class testEvaluateDiscard(TestCase):
    def setUp(self) -> None:
        self.discard = EvaluateDiscard()
        self.numbers = [Card(CardType.Number, i) for i in range(10)]
        self.cards = [
            Card(CardType.King),
            Card(CardType.Knight),
            Card(CardType.Dragon),
            Card(CardType.SleepingPotion),
            Card(CardType.MagicWand)
        ]

    def test_1card(self):
        for c in self.cards + self.numbers:
            self.assertTrue(self.discard.validDiscard([c]))

    def test_2Cards(self):
        for c1 in self.cards + self.numbers:
            for c2 in self.cards + self.numbers:
                self.assertEqual(self.discard.validDiscard([c1, c2]), c1 == c2)

    def test_moreCards(self):
        for c1 in self.cards:
            for c2 in self.cards + self.numbers:
                for c3 in self.cards + self.numbers:
                    self.assertFalse(self.discard.validDiscard([c1, c2, c3]))

        for c1 in self.numbers:
            for c2 in self.numbers:
                for c3 in self.numbers:
                    self.assertEqual(self.discard.validDiscard([c1, c2, c3]), c1.value + c2.value == c3.value)
