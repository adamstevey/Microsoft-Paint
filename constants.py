import os
import pygame

# CONSTANTS
WIDTH, HEIGHT = (900, 500)

TOOLBAR_HEIGHT = 40
BUTTON_PADDING = 1
BUTTON_GROUP_SEPARATION = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
GREY = (200, 200, 200)

TOOLBAR_GREY = (233, 233, 233)
HOVER_GREY = (200, 200, 200)
SELECTED_BLUE = (200, 200, 220)

DRAW_WIDTH = 10
SELECTED_COLOR = BLACK

# IMAGES
circleicon = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'c.png')), (40, 40))
pencilicon = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'pencil-icon.png')), (40, 40))
lineicon = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'line-icon.png')), (40, 40))
recticon = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'rect-icon.png')), (38, 38))
erasericon = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'eraser-icon.png')), (36, 36))
clearicon = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'clear-icon.png')), (38, 38))