from constants import *

class Line:
    def __init__(self):
        self.selected = False
        self.set_size = False
        self.start = None
        self.width = DRAW_WIDTH
        self.color = BLACK