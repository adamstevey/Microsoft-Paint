import pygame
import math

from constants import *

# TOOLS
class Clear:
    def __init__(self):
        self.selected = False

from button import Button
from eraser import Eraser
from circle import Circle
from pencil import Pencil
from rectangle import Rectangle
from line import Line


pygame.init()

###########
# OBJECTS #
###########

# TOOLS
line = Line()
pencil = Pencil()
circle = Circle()
rectangle = Rectangle()
eraser = Eraser()
clear = Clear()

fill = Fill()

tools = [line, pencil, circle, rectangle, eraser, clear]
widths = [10, 20, 30]
colors = [BLACK, BLUE, RED, GREEN, YELLOW, PURPLE, GREY]

# BUTTONS
# TOOL BUTTONS
icons = [lineicon, pencilicon, circleicon, recticon, erasericon, clearicon]
buttons = [Button(i * TOOLBAR_HEIGHT, 0, TOOLBAR_HEIGHT, TOOLBAR_HEIGHT, icons[i]) for i in range(len(tools))]

# WIDTH BUTTONS
widthx = len(tools)
width_buttons = [Button(i * TOOLBAR_HEIGHT + BUTTON_GROUP_SEPARATION, 0, TOOLBAR_HEIGHT, TOOLBAR_HEIGHT, None)
                 for i in range(widthx, widthx+len(widths))]

# COLOR BUTTONS
colorx = len(tools) + len(widths)
color_buttons = [Button(i * TOOLBAR_HEIGHT + 2* BUTTON_GROUP_SEPARATION, 0, TOOLBAR_HEIGHT, TOOLBAR_HEIGHT, None)
                 for i in range(colorx, colorx + len(colors))]

allbuttons = [buttons, width_buttons, color_buttons]

# DRAWINGS

items = []

# FUNCTIONS
def handle_colors():
    global SELECTED_COLOR
    for i in range(len(color_buttons)):
        if color_buttons[i].isOver(pos):
            color_buttons[i].selected = True
            SELECTED_COLOR = colors[i]
            for j in range(len(color_buttons)):
                if j != i:
                    color_buttons[j].selected = False

def draw_widths_and_colors():
    x = width_buttons[0].x + TOOLBAR_HEIGHT /2
    y = TOOLBAR_HEIGHT/2
    for i in range(len(width_buttons)):
        pygame.draw.circle(WIN, SELECTED_COLOR, (x, y), widths[i]/2)
        x += TOOLBAR_HEIGHT
    x = color_buttons[0].x + TOOLBAR_HEIGHT/2
    for i in range(len(color_buttons)):
        pygame.draw.circle(WIN, colors[i], (x, y), DRAW_WIDTH/2)
        x += TOOLBAR_HEIGHT

def update_widths_and_colors():
    for item in tools:
        item.width = DRAW_WIDTH
        if item != eraser:
            item.color = SELECTED_COLOR

def handle_widths(pos):
    global DRAW_WIDTH
    for i in range(len(width_buttons)):
        if width_buttons[i].isOver(pos):
            width_buttons[i].selected = True
            DRAW_WIDTH = widths[i]
            for j in range(len(width_buttons)):
                if j != i:
                    width_buttons[j].selected = False

def draw_toolbar():
    pygame.draw.rect(WIN, TOOLBAR_GREY, (0, 0, WIDTH, TOOLBAR_HEIGHT))
    for group in allbuttons:
        for button in group:
            button.draw()
    draw_widths_and_colors()

def handle_eraser():
    eraser.draw = False
    pressed = pygame.mouse.get_pressed()
    for item in pressed:
        if item == True:
            eraser.draw = True
    if eraser.draw:
        items.append((pos, eraser.width / 2, eraser.color,  'circle'))

def draw_items():
    for item in items:
        if item[-1] == 'circle':
            pygame.draw.circle(WIN, item[2], item[0], item[1])
        if item[-1] == 'line':
            pygame.draw.line(WIN, item[2], item[1], item[0], item[3])
        if item[-1] == 'rectangle':
            pygame.draw.rect(WIN, item[4], (item[0], item[1], item[2], item[3]))

def handle_clear():
    global items
    items = []
    clear.selected = False

def handle_pencil():
    pencil.draw = False
    pressed = pygame.mouse.get_pressed()
    for item in pressed:
        if item == True:
            pencil.draw = True
    if pencil.draw:
        items.append((pos, pencil.width / 2, pencil.color, 'circle'))

def new_line():
    if pos[1] > TOOLBAR_HEIGHT:
        if line.set_size:
            items.append((line.start, pos, line.color, line.width, 'line'))
            line.set_size = False
        else:
            line.start = pos
            line.set_size = True

def show_line_size():
    pygame.draw.line(WIN, line.color, line.start, pos, line.width)

def show_circle_size():
        radius = math.sqrt((circle.mid[0] - pos[0])**2 + (circle.mid[1] - pos[1])**2)
        circle.radius = radius
        pygame.draw.circle(WIN, circle.color, (circle.mid), circle.radius)
        pygame.draw.circle(WIN, circle.fill, (circle.mid), circle.radius - DRAW_WIDTH)

def show_rectangle_size():
    rectangle.get_coords(pos)
    pygame.draw.rect(WIN, rectangle.color, (rectangle.x, rectangle.y, rectangle.length, rectangle.height))
    pygame.draw.rect(WIN, rectangle.fill, (rectangle.x + rectangle.width, rectangle.y + rectangle.width,
                                           rectangle.length - 2* rectangle.width, rectangle.height - 2* rectangle.width))

def new_circle():
    if pos[1] > TOOLBAR_HEIGHT:
        if circle.set_size:
            radius = math.sqrt((pos[1] - circle.mid[1]) ** 2 + (pos[0] - circle.mid[0]) ** 2)
            items.append((circle.mid, radius, circle.color, 'circle'))
            items.append((circle.mid, radius - DRAW_WIDTH, circle.fill, 'circle'))
            circle.set_size = False

        else:
            circle.mid = pos
            circle.set_size = True

def new_rect():
    if pos[1] > TOOLBAR_HEIGHT:
        if rectangle.set_size:
            rectangle.get_coords(pos)

            items.append((rectangle.x, rectangle.y, rectangle.length, rectangle.height, rectangle.color, 'rectangle'))
            items.append((rectangle.x + rectangle.width, rectangle.y + rectangle.width, rectangle.length - 2* rectangle.width
                          , rectangle.height - 2* rectangle.width, rectangle.fill, 'rectangle'))
            rectangle.set_size = False

        else:
            rectangle.point = pos
            rectangle.set_size = True

def handle_tools(pos):

    # SELECT TOOLS
    for i in range(len(buttons)):
        if buttons[i].isOver(pos):
            buttons[i].selected = True
            tools[i].selected = True

            # DESELECT OTHERS
            for j in range(len(buttons)):
                if j != i:
                    buttons[j].selected = False
                    tools[j].selected = False

def create_win():
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Paint')
    return WIN

def draw_back(WIN, pos):
    global line
    # BACKGROUND
    WIN.fill(WHITE)

    draw_items()

    # SHOW CIRCLE SIZE
    if circle.set_size and circle.selected:
        show_circle_size()

    # SHOW LINE SIZE
    if line.set_size and line.selected:
        show_line_size()

    if rectangle.set_size and rectangle.selected:
        show_rectangle_size()

    draw_toolbar()

    pygame.display.update()

# MAIN LOOP
run = True

while run:
    pos = pygame.mouse.get_pos()
    WIN = create_win()

    draw_back(WIN, pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # HANDLE BUTTONS
            handle_tools(pos)
            handle_widths(pos)
            handle_colors()

            if circle.selected:
                new_circle()
            if line.selected:
                new_line()
            if rectangle.selected:
                new_rect()

    if pencil.selected:
        handle_pencil()

    if eraser.selected:
        handle_eraser()

    if clear.selected:
        handle_clear()

    update_widths_and_colors()
pygame.quit()
