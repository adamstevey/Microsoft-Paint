from constants import *

class Button:
    def __init__(self, x, y, width, height, icon):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.selected = False
        self.icon = icon

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def draw(self, WIN, pos):
        pygame.draw.rect(WIN, (0, 0, 0), (self.x, self.y, self.width, self.height))
        if self.isOver(pos):
            pygame.draw.rect(WIN, HOVER_GREY, (self.x + BUTTON_PADDING, self.y + BUTTON_PADDING,
                                               self.width - 2* BUTTON_PADDING, self.height - 2* BUTTON_PADDING))
        elif self.selected:
            pygame.draw.rect(WIN, SELECTED_BLUE, (self.x + BUTTON_PADDING, self.y + BUTTON_PADDING,
                                               self.width - 2 * BUTTON_PADDING, self.height - 2 * BUTTON_PADDING))
        else:
            pygame.draw.rect(WIN, TOOLBAR_GREY, (self.x + BUTTON_PADDING, self.y + BUTTON_PADDING,
                                               self.width - 2 * BUTTON_PADDING, self.height - 2 * BUTTON_PADDING))
        if self.icon != None:
            WIN.blit(self.icon, (self.x, self.y))