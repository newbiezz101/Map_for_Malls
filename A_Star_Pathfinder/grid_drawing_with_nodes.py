import pygame
from math import inf

# ---------------------- Defining colors ---------------------------------------

WALL = BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 111, 255)
ORANGE = (255, 128, 0)
PURPLE = (128, 0, 255)
YELLOW = (255, 255, 0)
GREY = (143, 143, 143)
BROWN = (186, 127, 50)
DARK_GREEN = (0, 128, 0)
DARKER_GREEN = (0, 50, 0)
DARK_BLUE = (0, 0, 128)

# ------------------------- Declaring window properties -------------------------------
SCREEN_HEIGHT = 550
SCREEN_WIDTH = 1254
GRID_WIDTH = 100
GRID_HEIGHT = GRID_WIDTH
ROWS = SCREEN_HEIGHT // GRID_HEIGHT
COLUMNS = SCREEN_WIDTH // GRID_WIDTH
BUTTON_HEIGHT = 50
WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Defining window size with extra space for buttons


# ----------------------------- Creating Nodes class ------------------------------------
class Node:
    nodetypes = ['blank', 'start', 'end', 'wall']

    colors = {
        'regular': {'blank': WHITE, 'start': RED, 'end': LIGHT_BLUE, 'wall': BLACK},
        'visited': {'blank': GREEN, 'start': RED, 'end': LIGHT_BLUE, 'wall': BLACK},
        'path': {'blank': BLUE, 'start': RED, 'end': LIGHT_BLUE, 'wall': BLACK}
    }

    distance_modifiers = {'blank': 1, 'start': 1, 'end': 1, 'wall': inf}

    def __init__(self, nodetype, text='', colors=colors, dmf=distance_modifiers):
        self.nodetype = nodetype
        self.rcolor = colors['regular'][self.nodetype]
        self.vcolor = colors['visited'][self.nodetype]
        self.pcolor = colors['path'][self.nodetype]
        self.is_visited = True if nodetype == 'start' else True if nodetype == 'end' else False
        self.is_path = True if nodetype == 'start' else True if nodetype == 'end' else False
        self.distance_modifier = dmf[self.nodetype]
        self.color = self.pcolor if self.is_path else self.vcolor if self.is_visited else self.rcolor

    def update(self, nodetype=False, is_visited='unchanged', is_path='unchanged', colors=colors, dmf=distance_modifiers,
               nodetypes=nodetypes):
        if nodetype:
            assert nodetype in nodetypes, f"nodetype must be one of: {nodetypes}"
            if (self.nodetype == ('start' or 'end')) and (nodetype == ('wall' or 'mud')):
                pass
            else:
                self.nodetype = nodetype

        if is_visited != 'unchanged':
            assert type(is_visited) == bool, "'is_visited' must be boolean: True or False"
            self.is_visited = is_visited

        if is_path != 'unchanged':
            assert type(is_path) == bool, "'is_path' must be boolean: True or False"
            self.is_path = is_path

        self.rcolor = colors['regular'][self.nodetype]
        self.vcolor = colors['visited'][self.nodetype]
        self.pcolor = colors['path'][self.nodetype]
        self.distance_modifier = dmf[self.nodetype]
        self.color = self.pcolor if self.is_path else self.vcolor if self.is_visited else self.rcolor


# ------------------------- Declaring a 2-dimensional array --------------------------
grid = []

for row in range(ROWS):
    grid.append([])
    for column in range(COLUMNS):
        grid[row].append(Node('blank'))

print(grid)


# ---------------------------- Draw function ------------------------------------------
def draw_square(row, column, color, fill=1):
    pygame.draw.rect(
        window,
        color,
        [
            GRID_WIDTH * column,
            GRID_HEIGHT * row,
            GRID_WIDTH,
            GRID_HEIGHT
        ],
        fill
    )


# ---------------------------- Initialising pygame ------------------------------------
pygame.init()

FONT = pygame.font.SysFont('arial', 6)
image = pygame.image.load("suriaconcoursemap.png")
window = pygame.display.set_mode(WINDOW_SIZE)  # setting up the screen
window.blit(image, [0, 0])  # loading image on the screen

# ----------------------------- Drawing walls/maze -----------------------------------------
wall = [[0, 0], [1, 1], [2, 2]]  # wall coordinates

for i in range(len(wall)):  # drawing the walls based on the wall coordinates
    grid[wall[i - 1][0]][wall[i - 1][1]].update(nodetype='wall')
    draw_square(wall[i - 1][0], wall[i - 1][1], WALL, fill=0)
    # print(f"[{wall[i - 1][0]}, {wall[i - 1][1]}]") #  checking the wall coordinate being drawn

print(grid)
pygame.display.flip()  # display the pygame drawing

done = False

# ------------------------- Main Program Loop Start ---------------------------------
while not done:
    for event in pygame.event.get():
        # print(grid)
        if event.type == pygame.QUIT:
            done = True

# ------------------------- Main Program Loop End -----------------------------------
