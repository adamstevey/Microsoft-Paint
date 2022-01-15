from constants import *

class Rectangle:
    def __init__(self):
        self.selected = False
        self.set_size = False
        self.width = DRAW_WIDTH
        self.point = None
        self.color = SELECTED_COLOR
        self.fill = WHITE
        self.x = None
        self.y = None
        self.length = None
        self.height = None

    def get_coords(self, pos):
        self.length = abs(pos[0] - self.point[0])
        self.height = abs(pos[1] - self.point[1])
        if pos[0] > self.point[0] and pos[1] > self.point[1]:
            self.x, self.y = self.point
        elif pos[0] > self.point[0] and pos[1] < self.point[1]:
            self.x, self.y = (self.point[0], pos[1])
        elif pos[0] < self.point[0] and pos[1] > self.point[1]:
            self.x, self.y = (pos[0], self.point[1])
        else:
            self.x, self.y = (pos)
