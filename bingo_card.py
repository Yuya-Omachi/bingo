
from abc import ABC, abstractmethod


class BingoCell(ABC):
    def __init__(self, is_opened: bool) -> None:
        self.is_opened = is_opened

    @abstractmethod
    def __str__(self) -> str:
        pass


class NumberCell(BingoCell):
    def __init__(self, is_opened: bool, number: int) -> None:
        super().__init__(is_opened)
        self.number = number

    def __str__(self) -> str:
        if super().is_opened:
            return f"({self.number.__str__()})"
        else:
            return self.number.__str__()


class FreeCell(BingoCell):
    def __init__(self, is_opened: bool) -> None:
        super().__init__(is_opened)

    def __str__(self) -> str:
        return "FREE"
