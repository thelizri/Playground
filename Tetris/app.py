# Import required libraries
import pygame
from tetris import Tetris
from constants import *


class App:
    def __init__(self):
        pygame.init()  # Initialize pygame

        self.display = pygame.display.set_mode(
            (GAME_WIDTH * TILE_SIZE + 200, GAME_HEIGHT * TILE_SIZE)
        )
        pygame.display.set_caption("TETRIS")
        self.game = Tetris(self.display)

    def draw_window(self):
        """This method is responsible for drawing the game board."""

        self.display.fill(BACKGROUND_COLOR)

        # Draw grid lines for the game board
        for x in range(GAME_WIDTH):
            for y in range(GAME_HEIGHT):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.display, TILE_COLOR, rect, 1)

    def main(self):
        """This is the main game loop."""
        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    self.game.handle_keydown_event(event)

            self.draw_window()
            self.game.draw_game()
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    app = App()  # Create an instance of the App class
    app.main()  # Start the main game loop
