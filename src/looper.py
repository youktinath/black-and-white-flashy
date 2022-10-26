from utils import *
import numpy as np
import math

def create_board_list(stable_prob=0.8, num_boards=10):
    init_board = create_random_board()
    board_list = [init_board]

    for i in range(num_boards):
        if stable_prob:
            prob = stable_prob
        else:
            # prob = np.random.uniform(size=1) / 4.
            prob = np.abs(np.sin(2 * i * math.pi / num_boards))
        next_board = alter_with_prob(init_board, prob)
        board_list.append(next_board)
        init_board = next_board

    return board_list