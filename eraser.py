from constants import *

class Eraser:
    def __init__(self):
        self.selected = False
        self.width = DRAW_WIDTH
        self.draw = False
        self.color = WHITE
