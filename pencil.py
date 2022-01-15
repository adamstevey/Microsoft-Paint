from constants import *

class Pencil:
    def __init__(self):
        self.selected = False
        self.draw = False
        self.width = DRAW_WIDTH
        self.color = BLACK