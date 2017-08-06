import numpy as np
import sys
import pygame
from pygame.locals import *


class Board:
    def __init__(self, size, starting=[], random=False):
        self.sizex, self.sizey = size
        self.size = size
        self.board = np.zeros(shape=self.size, dtype=np.int8)

        for pos in starting:
            self.board[pos[0], pos[1]] = 1

    def _count_neighbours(self):
        temp = np.pad(self.board, (1,1), 'constant', constant_values=(0, 0))
        neighbours = temp[:-2, :-2] + \
            temp[:-2, 1:-1] + \
            temp[:-2, 2:] + \
            temp[1:-1, :-2] + \
            temp[1:-1, 2:] + \
            temp[2:, :-2] + \
            temp[2:, 1:-1] + \
            temp[2:, 2:]
        return neighbours

    def evolve(self):
        pass


if __name__ == '__main__':
    GLIDER = [[3, 1], [3, 2], [3, 3], [2, 3], [1, 2]]
    board = Board((5, 5), GLIDER)

    print(board.board, '\n')

    print(board._count_neighbours())