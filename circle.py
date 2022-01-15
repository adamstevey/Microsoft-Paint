from constants import *

class Circle:
    def __init__(self):
        self.selected = False
        self.set_size = False
        self.mid = None
        self.radius = None
        self.color = BLACK
        self.width = DRAW_WIDTH
        self.fill = WHITE