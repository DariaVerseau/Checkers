import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#rgb
MILK = (255, 255, 224)
WHITE = (255, 255, 255)
BLACK = (100, 9, 0)
BLUE = (0, 0, 225)
GREY = (128, 128, 128)
D_BLACK = (0, 0, 0)

CROWN = pygame.transform.scale(pygame.image.load('img/crown.png'), (44, 30))