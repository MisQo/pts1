from dataclasses import dataclass
from enum import Enum


@dataclass
class CardType(Enum):
    Number = 0
    King = 1
    Knight = 2
    SleepingPotion = 3
    Dragon = 4
    MagicWand = 5
