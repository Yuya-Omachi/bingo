from bingo_card import *

card = BingoCard()

balls = list(range(1,76))
random.shuffle(balls)

card.print_cells()

for i, ball in enumerate(balls):
    card.fill_cell(ball)
    print(f"REACH: {card.count_reach_num()}")
    print(f"BINGO: {card.count_bingo_num()}")
    print("--------------------")
    print(f"ball[{i}]: {ball}")
    card.print_cells()
