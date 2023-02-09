from unittest import TestCase

from sleepingqueens.Card import Card
from sleepingqueens.CardType import CardType
from sleepingqueens.DrawingAndDiscardPile import DrawingAndDiscardPile
from sleepingqueens.Hand import Hand
from sleepingqueens.HandPosition import HandPosition


class testHand(TestCase):
    deck: DrawingAndDiscardPile
    cards: dict[HandPosition, Card]
    hand: Hand
    pick: list[HandPosition]

    def setUp(self) -> None:
        self.deck = DrawingAndDiscardPile([Card(CardType.Number, i) for i in range(10, 13)])
        self.cards = dict()
        for i in range(5):
            self.cards[HandPosition(i, 0)] = Card(CardType.Number, i)
        self.hand = Hand(0, self.cards, self.deck)
        self.pick = [HandPosition(1, 0), HandPosition(2, 0), HandPosition(4, 0)]

    def test_getCards(self):
        self.assertEqual(self.cards, self.hand.getCards())

    def test_hasCardOfType(self):
        cards = {
            HandPosition(0, 0): Card(CardType.King),
            HandPosition(1, 0): Card(CardType.Dragon),
            HandPosition(2, 0): Card(CardType.Knight)
        }
        hand = Hand(0, cards, self.deck)

        self.assertTrue(cards[hand.hasCardOfType(CardType.King)].type.value == CardType.King.value)
        self.assertTrue(cards[hand.hasCardOfType(CardType.Dragon)].type.value == CardType.Dragon.value)
        self.assertTrue(cards[hand.hasCardOfType(CardType.Knight)].type.value == CardType.Knight.value)

        self.assertEqual(hand.hasCardOfType(CardType.Number), None)
        self.assertEqual(hand.hasCardOfType(CardType.MagicWand), None)
        self.assertEqual(hand.hasCardOfType(CardType.SleepingPotion), None)

    def test_pickCards(self):
        expected = [Card(CardType.Number, 1), Card(CardType.Number, 2), Card(CardType.Number, 4)]
        got = self.hand.pickCards(self.pick)

        self.assertTrue(len(got) == 3)

        for i in range(3):
            self.assertTrue(got[i] in expected)
            self.assertTrue(expected[i] in got)

    def test_removePickedCardsAndRedraw(self):
        self.hand.removePickedCardsAndRedraw(self.pick)

        drawn = self.hand.pickCards(self.pick)
        expected = [Card(CardType.Number, i) for i in range(10, 13)]

        self.assertTrue(len(drawn) == 3)

        for i in range(3):
            self.assertTrue(drawn[i] in expected)
            self.assertTrue(expected[i] in drawn)

        self.assertEqual(self.hand.getCards()[HandPosition(0, 0)], Card(CardType.Number, 0))
        self.assertEqual(self.hand.getCards()[HandPosition(3, 0)], Card(CardType.Number, 3))
