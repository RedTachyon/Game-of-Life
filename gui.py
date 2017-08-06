import sys
import pygame
from pygame.locals import *
import numpy as np

from game import Board, GLIDER, GLIDER2

WINDOW_WIDTH = 801
WINDOW_HEIGHT = 801

BOARD_WIDTH = 50
BOARD_HEIGHT = 50

CELL_WIDTH = WINDOW_WIDTH // BOARD_WIDTH
CELL_HEIGHT = WINDOW_HEIGHT // BOARD_HEIGHT

FPS = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DEAD = (15, 15, 100)
ALIVE = (15, 100, 15)
GRID_COLOR = (55, 55, 55)

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Game of Life')
# To do: refactor the whole thing to OOP, optimize


def draw_horizontal_line(surface, y):
    pygame.draw.line(surface, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))


def draw_vertical_line(surface, x):
    pygame.draw.line(surface, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT))


def draw_grid():
    stepy = WINDOW_HEIGHT // BOARD_HEIGHT
    stepx = WINDOW_WIDTH // BOARD_WIDTH
    for i in range(BOARD_HEIGHT + 1):
        draw_horizontal_line(DISPLAYSURF, i * stepy)
    for i in range(BOARD_WIDTH + 1):
        draw_vertical_line(DISPLAYSURF, i * stepx)


def draw_square(surface, topleft, side, color):
    pygame.draw.rect(surface, color, (topleft, (topleft[0] + side, topleft[1] + side)))


def draw_board(surface, board):
    colors = {
        0: DEAD,
        1: ALIVE
    }
    for (y, x), val in np.ndenumerate(board.board):
        draw_square(surface, (x * CELL_WIDTH, y * CELL_HEIGHT), CELL_WIDTH, colors[val])


def main():
    DISPLAYSURF.fill(DEAD)

    clock = pygame.time.Clock()

    board = Board((BOARD_WIDTH, BOARD_HEIGHT), GLIDER)

    draw_board(DISPLAYSURF, board)
    draw_grid()
    pygame.display.update()

    running = True

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and running:
                running = False
            elif event.type == KEYDOWN and not running:
                running = True

        if running:
            board.evolve()
            draw_board(DISPLAYSURF, board)
            draw_grid()

            pygame.display.update()

            clock.tick(FPS)


if __name__ == '__main__':
    main()