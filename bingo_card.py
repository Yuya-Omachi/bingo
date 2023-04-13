
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

    # 数字をチェックし、合っているなら穴を開ける
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

    def fill_cell(self, number: int) -> None:
        # 各セルにopenメソッドを適用
        fill = lambda e: e.open(number)
        vfunc = np.vectorize(fill)
        vfunc(self.cells)

    def count_filled_in_line(self, line_indexes: list[tuple[int,int]]) -> int:
        filled = 0
        for index in line_indexes:
            # indexに対応したマスが開いているなら1を足し合わせる
            filled += 1 if self.cells[index[0],index[1]].is_opened else 0
        return filled

    def count_bingo_num(self) -> int:
        bingo_line_num = 0
        check_lines = [
            [(0,0),(0,1),(0,2),(0,3),(0,4)],
            [(1,0),(1,1),(1,2),(1,3),(1,4)],
            [(2,0),(2,1),(2,2),(2,3),(2,4)],
            [(3,0),(3,1),(3,2),(3,3),(3,4)],
            [(0,0),(1,0),(2,0),(3,0),(4,0)],
            [(0,1),(1,1),(2,1),(3,1),(4,1)],
            [(0,2),(1,2),(2,2),(3,2),(4,2)],
            [(0,3),(1,3),(2,3),(3,3),(4,3)],
            [(0,0),(1,1),(2,2),(3,3),(4,4)],
            [(0,4),(1,3),(2,2),(3,1),(4,0)]
        ]
        for line in check_lines:
            # 開いているマスが5つの列をビンゴとしてカウント
            bingo_line_num += 1 if self.count_filled_in_line(line) == 5 else 0
        return bingo_line_num

    def count_reach_num(self) -> int:
        reach_line_num = 0
        check_lines = [
            [(0,0),(0,1),(0,2),(0,3),(0,4)],
            [(1,0),(1,1),(1,2),(1,3),(1,4)],
            [(2,0),(2,1),(2,2),(2,3),(2,4)],
            [(3,0),(3,1),(3,2),(3,3),(3,4)],
            [(0,0),(1,0),(2,0),(3,0),(4,0)],
            [(0,1),(1,1),(2,1),(3,1),(4,1)],
            [(0,2),(1,2),(2,2),(3,2),(4,2)],
            [(0,3),(1,3),(2,3),(3,3),(4,3)],
            [(0,0),(1,1),(2,2),(3,3),(4,4)],
            [(0,4),(1,3),(2,2),(3,1),(4,0)]
        ]
        for line in check_lines:
            # 開いているマスが5つの列をビンゴとしてカウント
            reach_line_num += 1 if self.count_filled_in_line(line) == 4 else 0
        return reach_line_num