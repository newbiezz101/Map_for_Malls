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


# -------------------- Class for creating Button ---------------------------------
class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the Button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x, self.y, self.width, self.height), 0)

        pygame.draw.rect(win, self.color, (self.x + 1, self.y + 1, self.width - 1, self.height - 1), 0)

        if self.text != '':
            font = pygame.font.SysFont('arial', 12)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + int(self.width / 2 - text.get_width() / 2),
                self.y + int(self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


# -------------------------- class end ------------------------------------------------------


# ------------------------- Declaring window properties -------------------------------
SCREEN_HEIGHT = 550
SCREEN_WIDTH = 1254
GRID_WIDTH = 10
GRID_HEIGHT = GRID_WIDTH
ROWS = SCREEN_HEIGHT // GRID_HEIGHT
COLUMNS = SCREEN_WIDTH // GRID_WIDTH
BUTTON_HEIGHT = 50
WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT + 2 * BUTTON_HEIGHT)  # Defining window size with extra space for buttons

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

# ---------------------------- Defining & Drawing Buttons -----------------------------------------

Find = Button(GREY, 0, SCREEN_HEIGHT, SCREEN_WIDTH / 3, BUTTON_HEIGHT, 'Find')
Clear = Button(GREY, SCREEN_WIDTH / 3, SCREEN_HEIGHT, SCREEN_WIDTH / 3, BUTTON_HEIGHT, 'Clear')
Wall = Button(GREY, 2 * SCREEN_WIDTH / 3, SCREEN_HEIGHT, SCREEN_WIDTH / 3, BUTTON_HEIGHT, 'Wall')
Start = Button(RED, 0, SCREEN_HEIGHT + BUTTON_HEIGHT, SCREEN_WIDTH / 2, BUTTON_HEIGHT, 'Start Point')
End = Button(LIGHT_BLUE, SCREEN_WIDTH / 2, SCREEN_HEIGHT + BUTTON_HEIGHT, SCREEN_WIDTH / 2, BUTTON_HEIGHT, 'End Point')

Find.draw(window)
Clear.draw(window)
Wall.draw(window)
Start.draw(window)
End.draw(window)

pygame.display.flip()

# ----------------------------- Drawing walls/maze -----------------------------------------
count = 0
WALLS = 4

wall = []
maze = []


for i in range(WALLS):
    wall.append([])

wall[0] = [[0, 0], [1, 1], [2, 2], [1, 2], [2, 3], [3, 4]]
wall[1] = [[2, 3], [3, 4], [4, 5], [5, 6]]
wall[2] = [[6, 7], [7, 8]]
wall[3] = [[3, 4], [1, 1], [0, 0], ]

for i in range(WALLS):
    maze.append(wall[i])

selected_wall = maze[count]  # wall coordinates

print(maze[count])
print(len(maze[count]))
print(len(selected_wall))


# for i in range(len(selected_wall)):  # drawing the walls based on the wall coordinates
#    grid[selected_wall[i][0]][selected_wall[i][1]] = inf
#    draw_square(selected_wall[i][0], selected_wall[i][1], WALL)

# pygame.display.flip()  # display the pygame drawing

# ------------------------- Main Program Loop Start ---------------------------------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # If click is inside window
            if Wall.isOver(pos):
                if count < WALLS:

                    print(count)

                    image = pygame.image.load("suriaconcoursemap.png")
                    window.blit(image, [0, 0])


                    selected_wall = maze[count]  # wall coordinates

                    for i in range(len(selected_wall)):  # drawing the walls based on the wall coordinates
                        grid[selected_wall[i][0]][selected_wall[i][1]] = inf
                        draw_square(selected_wall[i][0], selected_wall[i][1], WALL)

                    pygame.display.flip()  # display the pygame drawing

                    count += 1

                else:
                    count = 0

                    print(count)

                    image = pygame.image.load("suriaconcoursemap.png")
                    window.blit(image, [0, 0])

                    selected_wall = maze[count]  # wall coordinates

                    for i in range(len(selected_wall)):  # drawing the walls based on the wall coordinates
                        grid[selected_wall[i][0]][selected_wall[i][1]] = inf
                        draw_square(selected_wall[i][0], selected_wall[i][1], WALL)

                    pygame.display.flip()  # display the pygame drawing

                    count += 1

                    continue
                    #print(count)

# ------------------------- Main Program Loop End -----------------------------------
