# Import necessary modules
import pygame
import time

# Initialize pygame
pygame.init()

# Define window size constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

# Create the display window with given size and set its title
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello World")

# Define color constants

# Basic colors
black, white = (0, 0, 0), (255, 255, 255)
red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)
yellow, orange, purple = (255, 255, 0), (255, 165, 0), (128, 0, 128)

# Shades of gray
gray, light_gray, dark_gray = (128, 128, 128), (192, 192, 192), (64, 64, 64)

# Additional colors
cyan, magenta, lime = (0, 255, 255), (255, 0, 255), (0, 255, 0)
pink, brown, navy, teal, olive = (
    (255, 192, 203),
    (165, 42, 42),
    (0, 0, 128),
    (0, 128, 128),
    (128, 128, 0),
)

# Define fonts
calibri_font = pygame.font.SysFont("calibri", 64)
custom_font = pygame.font.Font("AttackGraffiti.ttf", 32)

# Define text
calibri_text = calibri_font.render("Dragons rule!", True, red)
custom_text = custom_font.render("Move the dragon", True, pink)

calibri_rect = calibri_text.get_rect()
calibri_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

custom_rect = custom_text.get_rect()
custom_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

# Load dragon images and get their rectangle objects
dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_image.convert()
dragon_left_rect = dragon_left_image.get_rect()
dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_image.convert()
dragon_right_rect = dragon_right_image.get_rect()

# Position dragons at left and right ends respectively
dragon_left_rect.topleft = (0, 0)
dragon_right_rect.topright = (WINDOW_WIDTH, 0)


# Fill the display with the olive color
display.fill(olive)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        # Exit conditions
        if event.type == pygame.QUIT:
            running = False

    # Move the left dragon
    dragon_left_rect.move_ip(10, 0)

    # Refresh the display with the background color
    display.fill(olive)

    # Add text to the screen
    display.blit(calibri_text, calibri_rect)
    display.blit(custom_text, custom_rect)

    # Render the dragons at their respective positions
    display.blit(dragon_left_image, dragon_left_rect)
    display.blit(dragon_right_image, dragon_right_rect)

    # Update the display
    pygame.display.update()

    # Delay to control game speed
    time.sleep(0.1)

# End game
pygame.quit()
