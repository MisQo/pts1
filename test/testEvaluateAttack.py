from unittest import TestCase

from sleepingqueens.AwokenQueenPosition import AwokenQueenPosition
from sleepingqueens.Card import Card
from sleepingqueens.CardType import CardType
from sleepingqueens.DrawingAndDiscardPile import DrawingAndDiscardPile
from sleepingqueens.EvaluateAttack import EvaluateAttack
from sleepingqueens.GameState import GameState
from sleepingqueens.Hand import Hand
from sleepingqueens.HandPosition import HandPosition
from sleepingqueens.PlayerState import PlayerState
from sleepingqueens.Queen import Queen
from sleepingqueens.SleepingQueenPosition import SleepingQueenPosition


class testEvaluateAttack(TestCase):
    def setUp(self) -> None:
        self.awokenqueens = {
            AwokenQueenPosition(0, 0): Queen(0),
            AwokenQueenPosition(1, 0): Queen(1),
            AwokenQueenPosition(2, 0): Queen(2),
            AwokenQueenPosition(0, 1): Queen(3)
        }
        self.sleepingQueens = {
            SleepingQueenPosition(0): Queen(10),
            SleepingQueenPosition(1): Queen(11),
            SleepingQueenPosition(2): Queen(12),
            SleepingQueenPosition(3): Queen(13)
        }
        self.players = [
            PlayerState(0, Hand({HandPosition(0, 0): Card(CardType.Dragon)},
                                DrawingAndDiscardPile([Card(CardType.Number, 0) for _ in range(3)]))),
            PlayerState(1, Hand({HandPosition(0, 1): Card(CardType.MagicWand)},
                                DrawingAndDiscardPile([Card(CardType.Number, 1) for _ in range(3)]))),
            PlayerState(2, Hand({}, DrawingAndDiscardPile([])))]
        self.gamestate = GameState(numberOfPlayers=3, onTurn=0, awokenQueens=self.awokenqueens,
                                   sleepingQueens=self.sleepingQueens, players=self.players)
        self.attack = EvaluateAttack()

    def test_dragonDefense(self):
        self.attack.attack(self.gamestate, CardType.Dragon, AwokenQueenPosition(0, 0), AwokenQueenPosition(2, 1))
        self.assertTrue(AwokenQueenPosition(0, 0) in self.gamestate.awokenQueens)
        self.assertTrue(AwokenQueenPosition(2, 1) not in self.gamestate.awokenQueens)
        self.assertEqual(self.gamestate.players[0].hand.getCards(), {HandPosition(0, 0): Card(CardType.Number, 0)})

    def test_wandDefense(self):
        self.attack.attack(self.gamestate, CardType.MagicWand, AwokenQueenPosition(0, 1), AwokenQueenPosition(2, 1))
        self.assertTrue(AwokenQueenPosition(0, 1) in self.gamestate.awokenQueens)
        self.assertTrue(AwokenQueenPosition(2, 1) not in self.gamestate.awokenQueens)
        self.assertEqual(self.gamestate.players[1].hand.getCards(), {HandPosition(0, 1): Card(CardType.Number, 1)})

    def test_succesfullAttack(self):
        self.attack.attack(self.gamestate, CardType.MagicWand, AwokenQueenPosition(0, 0), AwokenQueenPosition(2, 1))
        self.assertTrue(AwokenQueenPosition(0, 0) not in self.gamestate.awokenQueens)
        self.assertTrue(AwokenQueenPosition(2, 1) in self.gamestate.awokenQueens)
