# Import required libraries
import random
from itertools import cycle
from constants import *
from block import Block


class Tetrominoes:
    def __init__(self, x, y, display, grid):
        choice = random.choice(TETROMINO_CHOICES)
        self.color = random.choice(BLOCK_COLORS)
        self.shapes = cycle(TETROMINO_SHAPES[choice])

        self.x = x
        self.y = y
        self.display = display
        self.grid = grid
        self.saved_shape = None
        self.create_new_blocks()

    def move(self, x, y):
        self.x += x
        self.y += y
        for block in self.blocks:
            block.move(x, y)

    def get_blocks(self):
        return self.blocks

    def can_move(self, x, y):
        for block in self.blocks:
            if not block.can_move(x, y):
                return False
        return True

    def is_at_bottom(self):
        for block in self.blocks:
            if block.is_at_bottom():
                return True
        return False

    def draw(self):
        for block in self.blocks:
            block.draw_block()

    def add_to_grid(self):
        for block in self.blocks:
            block.add_to_grid()

    def create_new_blocks(self):
        shape = next(self.shapes)
        self.blocks = []
        for row_idx, row in enumerate(shape):
            for col_idx, column in enumerate(row):
                if column == 1:
                    block = Block(
                        self.x + col_idx,
                        self.y + row_idx,
                        self.color,
                        self.display,
                        self.grid,
                    )
                    self.blocks.append(block)

    def rotate(self):
        new_blocks = self.can_rotate()
        if new_blocks is not None:
            self.blocks = new_blocks

    def can_rotate(self):
        shape = next(self.shapes) if self.saved_shape is None else self.saved_shape

        result = []
        for rowIdx, row in enumerate(shape):
            for columnIdx, column in enumerate(row):
                if column == 1:
                    block = Block(
                        self.x + columnIdx,
                        self.y + rowIdx,
                        self.color,
                        self.display,
                        self.grid,
                    )
                    result.append(block)

        for block in result:
            if block.is_out_of_bounds() or block.is_occupied():
                self.saved_shape = shape
                return None

        self.saved_shape = None
        return result
