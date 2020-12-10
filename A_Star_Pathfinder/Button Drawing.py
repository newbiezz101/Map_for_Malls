import pygame

# ---------------------- Defining colors ---------------------------------------

BLACK = (0, 0, 0)
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
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
BUTTON_HEIGHT = 50
WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT + BUTTON_HEIGHT * 2)  # Defining window size with extra space for buttons

# ---------------------------- Initialising pygame ------------------------------------
pygame.init()

FONT = pygame.font.SysFont('arial', 6)
window = pygame.display.set_mode(WINDOW_SIZE)

done = False

# ---------------------------- Defining & Drawing Buttons -----------------------------------------

Find = Button(GREY, 0, SCREEN_HEIGHT, SCREEN_WIDTH / 3, BUTTON_HEIGHT, 'Find')
Clear = Button(GREY, SCREEN_WIDTH / 3, SCREEN_HEIGHT, SCREEN_WIDTH / 3, BUTTON_HEIGHT, 'Clear')
Wall = Button(GREY, 2*SCREEN_WIDTH / 3, SCREEN_HEIGHT, SCREEN_WIDTH / 3, BUTTON_HEIGHT, 'Wall')
Start = Button(RED, 0, SCREEN_HEIGHT + BUTTON_HEIGHT, SCREEN_WIDTH / 2, BUTTON_HEIGHT, 'Start Point')
End = Button(BLUE, SCREEN_WIDTH / 2, SCREEN_HEIGHT + BUTTON_HEIGHT, SCREEN_WIDTH / 2, BUTTON_HEIGHT, 'End Point')

Find.draw(window)
Clear.draw(window)
Wall.draw(window)
Start.draw(window)
End.draw(window)

pygame.display.flip()

# ------------------------- Main Program Loop Start ---------------------------------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

# ------------------------- Main Program Loop End -----------------------------------

