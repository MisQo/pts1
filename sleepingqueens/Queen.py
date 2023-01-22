from dataclasses import dataclass


@dataclass
class Queen:
    _points: int
    def getPoints(self) -> int:
        return self._points