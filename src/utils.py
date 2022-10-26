import numpy as np


def create_random_board(board_size=8):
    x = np.random.randint(0, 2, size=board_size * board_size)
    return x.reshape(board_size, board_size)

def alter_with_prob(board_state, prob=0.8):
    board_size = board_state.shape[0]
    will_alter = np.random.binomial(1, prob, size=board_size * board_size).reshape(board_size, board_size)
    return np.abs(board_state - will_alter)

# test
# board = create_random_board()
# print(board)
# print(alter_with_prob(board))