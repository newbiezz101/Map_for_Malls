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


# ------------------------- Declaring a 2-dimensional array --------------------------
grid = []

for row in range(ROWS):
    grid.append([])
    for column in range(COLUMNS):
        grid[row].append(1)

print(grid)


# ---------------------------- Draw function ------------------------------------------
def draw_square(row, column, color, fill=0):
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

done = False

# ----------------------------- Drawing walls/maze -----------------------------------------
wall = [[0, 0], [1, 1], [2, 2], [4, 11]]  # wall coordinates

for i in range(len(wall)):  # drawing the walls based on the wall coordinates
    grid[wall[i - 1][0]][wall[i - 1][1]] = inf
    draw_square(wall[i - 1][0], wall[i - 1][1], WALL)
    # print(f"[{wall[i - 1][0]}, {wall[i - 1][1]}]") #  checking the wall coordinate being drawn

print(grid)
pygame.display.flip()  # display the pygame drawing


# ------------------------- Main Program Loop Start ---------------------------------
while not done:
    for event in pygame.event.get():
        # print(grid)
        if event.type == pygame.QUIT:
            done = True

# ------------------------- Main Program Loop End -----------------------------------
