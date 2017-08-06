import numpy as np

GLIDER = ([3, 1], [3, 2], [3, 3], [2, 3], [1, 2])
GLIDER2 = ([2, 1], [2, 3], [3, 2], [3, 3], [4, 2])


class Board:
    def __init__(self, size, starting=tuple(), random=False):
        self.sizex, self.sizey = size
        self.size = size
        if random:
            self.board = np.random.randint(2, size=size)
        else:
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
        return neighbours.astype(np.int8)

    def evolve(self):
        neighbours = self._count_neighbours()
        survive_die = np.logical_not(np.round(neighbours - 2.5)).astype(np.int8)

        birth = np.copy(neighbours)
        birth[birth != 3] = 0
        birth = np.sign(birth).astype(np.int8)

        # print(survive_die, '\n')
        # print(birth, '\n')

        self.board = np.sign(self.board * survive_die + birth).astype(np.int8)

        return self.board


if __name__ == '__main__':
    board = Board((10, 10), GLIDER)

    print(board.board, '\n')
    print(board.evolve(), '\n')
    print(board.evolve(), '\n')
    print(board.evolve(), '\n')
    print(board.evolve(), '\n')
    print(board.evolve(), '\n')
    print(board.evolve(), '\n')
