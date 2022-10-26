from looper import *
import seaborn as sns
import matplotlib.pyplot as plt
import os

def visualize(try_folder, stable_prob=0.8, num_boards=10):
    board_list = create_board_list(stable_prob, num_boards)

    if not os.path.exists(f"./outputs/test1/{try_folder}"):
        os.mkdir(f"./outputs/test1/{try_folder}")
    os.chdir(f"./outputs/test1/{try_folder}")

    for i, board in enumerate(board_list):
        plt.figure(figsize=(10, 10))
        sns.heatmap(board, cbar=False, xticklabels=False, yticklabels=False)
        plt.savefig(f"board_{i}.png")
        plt.close()