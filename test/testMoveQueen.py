from unittest import TestCase

from sleepingqueens.AwokenQueenPosition import AwokenQueenPosition
from sleepingqueens.DrawingAndDiscardPile import DrawingAndDiscardPile
from sleepingqueens.GameState import GameState
from sleepingqueens.Hand import Hand
from sleepingqueens.MoveQueen import MoveQueen
from sleepingqueens.PlayerState import PlayerState
from sleepingqueens.Queen import Queen
from sleepingqueens.SleepingQueenPosition import SleepingQueenPosition


class testMoveQueen(TestCase):
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
            PlayerState(0, Hand({}, DrawingAndDiscardPile([]))),
            PlayerState(1, Hand({}, DrawingAndDiscardPile([]))),
            PlayerState(2, Hand({}, DrawingAndDiscardPile([])))
        ]
        self.gamestate = GameState(numberOfPlayers=3, onTurn=0, awokenQueens=self.awokenqueens,
                                   sleepingQueens=self.sleepingQueens, players=self.players)
        self.move = MoveQueen()

    def test_fromSleep(self):
        self.move.move(self.gamestate, SleepingQueenPosition(0), AwokenQueenPosition(0, 2))
        self.assertTrue(SleepingQueenPosition(0) not in self.gamestate.sleepingQueens)
        self.assertTrue(self.gamestate.awokenQueens[AwokenQueenPosition(0, 2)].getPoints() == 10)

    def test_toSleep(self):
        self.move.move(self.gamestate, AwokenQueenPosition(0, 0), SleepingQueenPosition(4))
        self.assertTrue(AwokenQueenPosition(0, 0) not in self.gamestate.awokenQueens)
        self.assertTrue(self.gamestate.sleepingQueens[SleepingQueenPosition(4)].getPoints() == 0)

    def test_playerToPlayer(self):
        self.move.move(self.gamestate, AwokenQueenPosition(2, 0), AwokenQueenPosition(1, 2))
        self.assertTrue(AwokenQueenPosition(2, 0) not in self.gamestate.sleepingQueens)
        self.assertTrue(self.gamestate.awokenQueens[AwokenQueenPosition(1, 2)].getPoints() == 2)
