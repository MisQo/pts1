from typing import Optional
from unittest import TestCase

from sleepingqueens.AwokenQueenPosition import AwokenQueenPosition
from sleepingqueens.Card import Card
from sleepingqueens.CardType import CardType
from sleepingqueens.DrawingAndDiscardPile import DrawingAndDiscardPile
from sleepingqueens.EvaluateAttack import EvaluateAttackInterface
from sleepingqueens.EvaluateDiscard import EvaluateDiscardInterface
from sleepingqueens.GameState import GameState
from sleepingqueens.Hand import Hand
from sleepingqueens.HandPosition import HandPosition
from sleepingqueens.MoveQueen import MoveQueenInterface
from sleepingqueens.Player import Player
from sleepingqueens.PlayerState import PlayerState
from sleepingqueens.Position import Position
from sleepingqueens.Queen import Queen
from sleepingqueens.SleepingQueenPosition import SleepingQueenPosition


class AlwaysFalse(EvaluateDiscardInterface):
    def validDiscard(self, cards: list[Card]) -> bool:
        return False


class AlwaysAttack(EvaluateAttackInterface):

    def attack(self, gamestate: GameState, defense: CardType, from_: AwokenQueenPosition,
               to: Position) -> None:
        move = AlwaysMove()
        move.move(gamestate, from_, to)


class AlwaysMove(MoveQueenInterface):

    def move(self, gamestate: GameState, from_: Optional[Position], to: Position) -> None:
        if isinstance(from_, SleepingQueenPosition):
            if isinstance(to, AwokenQueenPosition):
                gamestate.awokenQueens[to] = gamestate.sleepingQueens[from_]
                gamestate.sleepingQueens.pop(from_)

        elif isinstance(from_, AwokenQueenPosition):
            if isinstance(to, AwokenQueenPosition):
                gamestate.awokenQueens[to] = gamestate.awokenQueens[from_]
                gamestate.awokenQueens.pop(from_)
            elif isinstance(to, SleepingQueenPosition):
                gamestate.sleepingQueens[to] = gamestate.awokenQueens[from_]
                gamestate.awokenQueens.pop(from_)


class testPlayer(TestCase):
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
            PlayerState(0, Hand({HandPosition(0, 0): Card(CardType.King)},
                                DrawingAndDiscardPile([Card(CardType.Number, 0) for _ in range(3)]))),
            PlayerState(1, Hand({HandPosition(0, 1): Card(CardType.Knight)},
                                DrawingAndDiscardPile([Card(CardType.Number, 1) for _ in range(3)]))),
            PlayerState(2, Hand({HandPosition(0, 2): Card(CardType.SleepingPotion)},
                                DrawingAndDiscardPile([Card(CardType.Number, 1) for _ in range(3)])))]
        self.gamestate = GameState(numberOfPlayers=3, onTurn=0, awokenQueens=self.awokenqueens,
                                   sleepingQueens=self.sleepingQueens, players=self.players)

    def test_raiseNoCards(self):
        player = Player(0, AlwaysFalse(), AlwaysMove(), AlwaysAttack())
        with self.assertRaises(Exception):
            player.play(self.gamestate, [], True)

    def test_raiseInvalidDiscard(self):
        player = Player(0, AlwaysFalse(), AlwaysMove(), AlwaysAttack())
        with self.assertRaises(Exception):
            player.play(self.gamestate, [HandPosition(0, 0), HandPosition(1, 0)], True)

    def test_King(self):
        player = Player(0, AlwaysFalse(), AlwaysMove(), AlwaysAttack())
        player.play(self.gamestate, [HandPosition(0, 0)], False, SleepingQueenPosition(0))
        self.assertEqual(self.gamestate.awokenQueens[AwokenQueenPosition(3, 0)], Queen(10))

    def test_Knight(self):
        player = Player(1, AlwaysFalse(), AlwaysMove(), AlwaysAttack())
        player.play(self.gamestate, [HandPosition(0, 1)], False, AwokenQueenPosition(0, 0))
        self.assertEqual(self.gamestate.awokenQueens[AwokenQueenPosition(1, 1)], Queen(0))

    def test_Potion(self):
        player = Player(2, AlwaysFalse(), AlwaysMove(), AlwaysAttack())
        player.play(self.gamestate, [HandPosition(0, 2)], False, AwokenQueenPosition(1, 0))
        self.assertEqual(self.gamestate.sleepingQueens[SleepingQueenPosition(4)], Queen(1))
