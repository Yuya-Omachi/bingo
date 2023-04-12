
from abc import ABC, abstractmethod
import numpy as np
import random

# ビンゴカードの各マス
class BingoCell(ABC):
    def __init__(self, is_opened: bool) -> None:
        self.is_opened = is_opened

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def open(self, number: int) -> None:
        pass

# 数字の書かれたマス
class NumberCell(BingoCell):
    def __init__(self, number: int) -> None:
        super().__init__(is_opened=False)
        self.number = number

    def __str__(self) -> str:
        zerofilled = self.number.__str__().zfill(2)
        if self.is_opened:
            return f"({zerofilled})"
        else:
            return f" {zerofilled} "

    def open(self, number: int) -> None:
        if self.number == number:
            self.is_opened = True


# FREEのマス
class FreeCell(BingoCell):
    def __init__(self) -> None:
        super().__init__(is_opened=True)

    def __str__(self) -> str:
        return "FREE"

    def open(self, number: int) -> None:
        return super().open(number)


class BingoCard:
    def __init__(self) -> None:
        self.cells = self.init_cells()

    # マスの初期化
    def init_cells(self) -> np.ndarray:
        card = np.empty((5,5),dtype=BingoCell)
        firsts = [1,16,31,46,61]
        for i, first in enumerate(firsts):
            line = random.sample(range(first,first+15-1), k=5)
            line.sort()
            card[i] = [NumberCell(num) for num in line]
        card[2,2] = FreeCell()
        return card.T

    def print_cells(self) -> None:
        formatted = self.cells.astype('str')
        for line in formatted:
            print(*line)

