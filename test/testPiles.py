from copy import copy
from unittest import TestCase
import random

from sleepingqueens.CardType import CardType
from sleepingqueens.DrawingAndDiscardPile import DrawingAndDiscardPile, ConcreteStrategyB
from sleepingqueens.Card import Card


class testPile(TestCase):
    def setUp(self) -> None:
        self.drawPile = [Card(CardType.King), Card(CardType.Knight), Card(CardType.SleepingPotion)]
        self.discardPile = [Card(CardType.Dragon), Card(CardType.MagicWand)]
        self.hand = [Card(CardType.Number, 1), Card(CardType.Number, 2), Card(CardType.Number, 3)]

    def test_getDrawPile(self):
        deck = DrawingAndDiscardPile(copy(self.drawPile), copy(self.discardPile))
        self.assertEqual(deck.getDrawPile(), self.drawPile)

    def test_getDiscardPile(self):
        deck = DrawingAndDiscardPile(copy(self.drawPile), copy(self.discardPile))
        self.assertEqual(deck.getDiscardPile(), self.discardPile)

    def test_draw(self):
        deck = DrawingAndDiscardPile(copy(self.drawPile))
        self.assertEqual(deck.discardAndDraw(self.hand[:1]), self.drawPile[:1])
        self.assertEqual(deck.getDiscardPile(), self.hand[:1])
        self.assertTrue(len(deck.getDrawPile()) == len(self.drawPile) - 1)

        self.assertEqual(deck.discardAndDraw(self.hand[1:2]), self.drawPile[1:2])
        self.assertEqual(deck.discardAndDraw(self.hand[2:]), self.drawPile[2:])

        self.assertTrue(len(deck.getDrawPile()) == 0)

        # check if correct cards are in discard
        self.assertTrue(len(deck.getDiscardPile()) == 3)
        for i in range(3):
            self.assertTrue(self.hand[i] in deck.getDiscardPile())

    def test_shuffleA(self):
        deck = DrawingAndDiscardPile(copy(self.drawPile[:1]),
                                     [Card(CardType.Number, 4), Card(CardType.Number, 5), Card(CardType.Number, 6),
                                      Card(CardType.Number, 7)], 42)

        drawn = deck.discardAndDraw(self.hand)
        expected = [Card(CardType.King), Card(CardType.Number, 6), Card(CardType.Number, 5)]

        self.assertTrue(len(drawn) == 3)

        for i in range(3):
            self.assertTrue(drawn[i] in expected)
            self.assertTrue(expected[i] in drawn)

        self.assertEqual(deck.getDrawPile(), [Card(CardType.Number, 7), Card(CardType.Number, 4)])

        discard = deck.getDiscardPile()
        self.assertTrue(len(discard) == 3)
        for i in range(3):
            self.assertTrue(discard[i] in self.hand)
            self.assertTrue(self.hand[i] in discard)

    def test_shuffleB(self):
        deck = DrawingAndDiscardPile(copy(self.drawPile[:1]),
                                     [Card(CardType.Number, 4), Card(CardType.Number, 5), Card(CardType.Number, 6),
                                      Card(CardType.Number, 7)], 42, ConcreteStrategyB())

        '''random.seed(42)
        x = [Card(CardType.Number, 4), Card(CardType.Number, 5), Card(CardType.Number, 6),
             Card(CardType.Number, 7)] + self.hand
        random.shuffle(x)
        print(x)'''

        drawn = deck.discardAndDraw(self.hand)
        expected = [Card(CardType.King), Card(CardType.Number, 5), Card(CardType.Number, 7)]

        self.assertTrue(len(drawn) == 3)

        for i in range(3):
            self.assertTrue(drawn[i] in expected)
            self.assertTrue(expected[i] in drawn)

        self.assertEqual(deck.getDrawPile(),
                         [Card(CardType.Number, 1), Card(CardType.Number, 6), Card(CardType.Number, 3),
                          Card(CardType.Number, 4), Card(CardType.Number, 2)])

        discard = deck.getDiscardPile()
        self.assertTrue(len(discard) == 0)
