import pygame

WIDTH, HEIGHT = 720, 720
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# rgb
RED = (100, 0, 0)
WHITE = (255, 255, 255)
BLACK = (196, 118, 0)
BLUE = (138, 194, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(
    pygame.image.load("Python_Checkers_AI\\assets\\crown.png"), (44, 25)
)
