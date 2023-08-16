# Import required libraries
import pygame
from tetromine import Tetrominoes
from constants import *


class Tetris:
    def __init__(self, display):
        self.display = display
        self.blocks = []
        self.grid = [[False] * 10 for _ in range(16)]
        self.tetris = Tetrominoes(4, 0, self.display, self.grid)

    def handle_keydown_event(self, event):
        if event.key == pygame.K_DOWN:
            self.move_block(0, 1)
        elif event.key == pygame.K_LEFT:
            self.move_block(-1, 0)
        elif event.key == pygame.K_RIGHT:
            self.move_block(1, 0)
        elif event.key == pygame.K_UP:
            self.tetris.rotate()

    def draw_game(self):
        self.tetris.draw()
        for block in self.blocks:
            block.draw_block()

    def create_new_tetris(self):
        self.tetris.add_to_grid()
        self.blocks.extend(self.tetris.get_blocks())
        self.tetris = Tetrominoes(4, 0, self.display, self.grid)

    def move_block(self, x, y):
        if self.tetris.can_move(x, y):
            self.tetris.move(x, y)
        elif self.tetris.is_at_bottom() and y > 0:
            self.create_new_tetris()
            self.remove_completed_rows()

    def remove_completed_rows(self):
        rows_to_be_removed = []
        for row_idx, row in enumerate(self.grid):
            if all(row):
                self.blocks = list(
                    filter(lambda block: block.row != row_idx, self.blocks)
                )
                rows_to_be_removed.append(row_idx)
        if rows_to_be_removed:
            for row in reversed(rows_to_be_removed):
                self.grid.pop(row)
            for i in range(len(rows_to_be_removed)):
                self.grid.insert(0, [False] * 10)
            self.update_position_of_blocks()

    def update_position_of_blocks(self):
        for row_idx, row in enumerate(self.grid):
            for col_idx, block in enumerate(row):
                if block != False:
                    block.update_position(col_idx, row_idx)
