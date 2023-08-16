# Import required libraries
import pygame
from constants import *


class Block:
    def __init__(self, x, y, color, display, grid):
        self.rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.column = x
        self.row = y
        self.color = color
        self.display = display
        self.grid = grid

    def draw_block(self):
        pygame.draw.rect(self.display, self.color, self.rect, 0, border_radius=8)

    def update_position(self, x, y):
        self.row, self.column = y, x
        self.rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def move(self, x, y):
        horizontal_movement = x * TILE_SIZE
        vertical_movement = y * TILE_SIZE
        self.column += x
        self.row += y
        self.rect.move_ip((horizontal_movement, vertical_movement))

    def collision(self, x, y):
        try:
            return self.grid[self.row + y][self.column + x] != False
        except IndexError:
            print(
                f"Row: {self.row + y} Column: {self.column + x} len(grid): {len(self.grid)}"
            )

    def is_at_bottom(self):
        return self.row == BOTTOM_ROW or self.grid[self.row + 1][self.column]

    def add_to_grid(self):
        self.grid[self.row][self.column] = self

    def is_occupied(self):
        return self.grid[self.row][self.column] != False

    def is_out_of_bounds(self):
        if self.column < 0 or self.column >= GAME_WIDTH:
            return True
        if self.row < 0 or self.row >= GAME_HEIGHT:
            return True
        return False

    def can_move(self, x, y):
        if self.column + x >= 0 and self.column + x < GAME_WIDTH:
            if self.row + y >= 0 and self.row + y < GAME_HEIGHT:
                if not self.collision(x, y):
                    return True
        return False

    def move_down_a_row(self):
        if self.row != BOTTOM_ROW:
            self.move(0, 1)
