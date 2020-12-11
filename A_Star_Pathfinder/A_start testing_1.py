import pygame
import numpy as np
import time
from math import inf
import heapq
import json

# ---------------------- Defining colours ---------------------------------------

WALL_COLOUR = BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
START_COLOUR = GREEN = (0, 255, 0)
END_COLOUR = RED = (255, 0, 0)
BLUE = (0, 0, 255)
SCAN_COLOUR = LIGHT_BLUE = (0, 111, 255)
ORANGE = (255, 128, 0)
PURPLE = (128, 0, 255)
YELLOW = (255, 255, 0)
GREY = (143, 143, 143)
BROWN = (186, 127, 50)
DARK_GREEN = (0, 128, 0)
DARKER_GREEN = (0, 50, 0)
PATH_COLOUR = BLUE = (0, 0, 128)

algorithm_run = False
path_found = False
DIAGONALS = False
VISUALISE = False
ASTAR = True


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


# ---------------------------------------------------------------------------------------------------------------------

# -------------------------- Node class -------------------------------------------------------------------------------
class Node():
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
            if (self.nodetype == ('start' or 'end')) and (nodetype == 'wall'):
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


# ---------------------------------------------------------------------------------------------------------------------

# ------------------------- Declaring window properties -------------------------------
SCREEN_HEIGHT = 550
SCREEN_WIDTH = 1254
GRID_WIDTH = 10
GRID_HEIGHT = GRID_WIDTH
ROWS = SCREEN_HEIGHT // GRID_HEIGHT
COLUMNS = SCREEN_WIDTH // GRID_WIDTH
BUTTON_HEIGHT = 50
WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT + 2 * BUTTON_HEIGHT)  # Defining window size with extra space for buttons


# ------------------------ Appending blank nodes to the grid ----------------------------------------------------------
def grid_blank(grid):
    for row in range(ROWS):
        grid.append([])
        for column in range(COLUMNS):
            grid[row].append(Node('blank'))


# ------------------------- Declaring a 2-dimensional array --------------------------
grid = []

grid_blank(grid)


# ---------------------------- Draw function ------------------------------------------
def draw_square(row, column, colour, fill=0):
    pygame.draw.rect(
        window,
        colour,
        [
            GRID_WIDTH * column,
            GRID_HEIGHT * row,
            GRID_WIDTH,
            GRID_HEIGHT
        ],
        fill
    )


# ---------------------------- Update square drawing ---------------------------------
def update_square(row, column):
    pygame.display.update(
        GRID_WIDTH * column,
        GRID_HEIGHT * row,
        GRID_WIDTH,
        GRID_HEIGHT
    )


# ---------------------------- Drawing Start Point Function ---------------------------
def draw_start(start_point):
    global selected_start
    selected_start = start_point[count_start]
    grid[selected_start[0]][selected_start[1]].update(nodetype='start')
    draw_square(selected_start[0], selected_start[1], START_COLOUR)
    pygame.display.flip()


# ---------------------------- Drawing End Point Function -----------------------------
def draw_end(end_point):
    global selected_end
    selected_end = end_point[count_end]
    grid[selected_end[0]][selected_end[1]].update(nodetype='end')
    draw_square(selected_end[0], selected_end[1], END_COLOUR)
    pygame.display.flip()


# ---------------------------- Drawing Wall Function ----------------------------------
def draw_wall(wall):
    global selected_wall
    clear_nodes()
    selected_wall = wall[count_wall]
    for i in range(len(selected_wall)):  # drawing the walls based on the wall coordinates
        grid[selected_wall[i][0]][selected_wall[i][1]].update(nodetype='wall')
        draw_square(selected_wall[i][0], selected_wall[i][1], WALL_COLOUR)
    pygame.display.flip()  # display the pygame drawing


# ---------------------------------- Clearing the nodes and changing them back to 'blank' -----------------------------
def clear_nodes():
    for row in range(ROWS):
        for column in range(COLUMNS):
            if (row, column) != selected_start and (row, column) != selected_end:
                grid[row][column].update(nodetype='blank', is_visited=False, is_path=False)


# ---------------------------- Initialising pygame ------------------------------------
pygame.init()

FONT = pygame.font.SysFont('arial', 6)
image = pygame.image.load("suriaconcoursemap.png")
window = pygame.display.set_mode(WINDOW_SIZE)  # setting up the screen
window.blit(image, [0, 0])  # loading image on the screen

done = False

# ---------------------------- Defining & Drawing Buttons -----------------------------------------
# TODO: Add an 'Export Path' button to export shortest_path to JSON.
Find = Button(GREY, 0, SCREEN_HEIGHT, SCREEN_WIDTH / 3, BUTTON_HEIGHT, 'Find')
Clear = Button(GREY, SCREEN_WIDTH / 3, SCREEN_HEIGHT, SCREEN_WIDTH / 3, BUTTON_HEIGHT, 'Clear')
Wall = Button(GREY, 2 * SCREEN_WIDTH / 3, SCREEN_HEIGHT, SCREEN_WIDTH / 3, BUTTON_HEIGHT, 'Wall')
Start = Button(START_COLOUR, 0, SCREEN_HEIGHT + BUTTON_HEIGHT, SCREEN_WIDTH / 2, BUTTON_HEIGHT, 'Start Point')
End = Button(END_COLOUR, SCREEN_WIDTH / 2, SCREEN_HEIGHT + BUTTON_HEIGHT, SCREEN_WIDTH / 2, BUTTON_HEIGHT, 'End Point')

Find.draw(window)
Clear.draw(window)
Wall.draw(window)
Start.draw(window)
End.draw(window)

pygame.display.flip()

# ------------------------------ Initiating start and end point ---------------------------
start_point = end_point = \
    [(30, 2), (30, 4), (30, 6), (30, 7), (30, 8), (30, 12), (30, 16), (30, 18), (30, 21), (30, 24), (30, 30),
     (30, 32), (30, 38), (30, 44), (30, 50), (30, 52), (30, 54), (20, 56), (17, 56), (11, 60), (9, 62),
     (7, 60), (4, 74), (7, 74), (8, 74), (9, 74), (11, 74), (15, 74), (14, 93), (17, 74), (19, 74), (21, 74), (28, 74),
     (30, 83), (30, 85), (30, 88), (30, 90), (30, 92), (30, 99), (30, 101), (30, 105), (30, 111), (30, 118),
     (39, 122), (39, 119), (39, 116), (39, 113), (39, 110), (39, 107), (39, 104), (39, 101), (39, 98),
     (39, 91), (39, 86), (39, 83), (39, 75), (44, 70), (40, 65), (44, 60), (39, 55), (39, 45),
     (39, 40), (39, 35), (39, 31), (39, 24), (39, 21), (39, 18), (39, 13), (39, 10), (39, 7), (39, 5), (39, 2)
     ]

# end_point = [(30, 2), (30, 4), (30, 6), (30, 7), (30, 8), (30, 12), (30, 16), (30, 18), (30, 21), (30, 24), (30, 30),
#              (30, 32), (30, 38), (30, 44), (30, 50), (30, 52), (30, 54), (20, 56), (17, 56), (11, 60), (9, 62),
#              (7, 60), (4, 74), (7, 74), (8, 74), (9, 74), (11, 74), (15, 74), (17, 74), (19, 74), (21, 74), (28, 74),
#              (30, 83), (30, 85), (30, 88), (30, 90), (30, 92), (30, 99), (30, 101), (30, 105), (30, 111), (30, 118),
#              (39, 122), (39, 119), (39, 116), (39, 113), (39, 110), (39, 107), (39, 104), (39, 101), (39, 98),
#              (39, 91), (39, 86), (39, 83), (39, 75), (44, 70), (38, 70), (38, 60), (44, 60), (39, 55), (39, 45),
#              (39, 40), (39, 35), (39, 31), (39, 24), (39, 21), (39, 18), (39, 13), (39, 10), (39, 7), (39, 5), (39, 2)
#              ]


shops_name = ["LYSHA FLORA", "MINT COBBLER", "FOTOPOINT", "A", "B", "NANDOS", "FAMOUS AMOS", "UNIVERSAL TRAVELLER",
              "C", "AUNTIE ANNE", "PEDRO", "GIORDANO", "ISETAN", "NAF NAF", "G200 MEN", "VINCCI", "G200", "WATATIME",
              "KFC", "TOYS R US", "ATM1", "SURAU", "POS MALAYSIA", "YOSHI CONNECTION", "ENGLAND OPTICAL", "ATM2",
              "MAYBANK", "GUARDIAN", "MEMORY LANE", "BURGER KING", "COLD STORAGE", "SWATCH", "GAP", "EVITA PERONI",
              "FOCUS POINT", "MARKS & SPENCER", "LA SENZA", "LOREAL", "DUNKINS DONUTS", "LA CUCUR", "A&W",
              "SECRET RECIPE", "PIZZA HUT", "AL AMAN STATIONERY", "ANJUNG INTERNET JARING", "RUTH ALTERATION",
              "CRYSTAL CORNER", "SALAMATH MONEY CHANGER", "SOXWORLD", "VITACARE", "THE MANHATTAN FISH MARKET",
              "HIMALAYA", "MNG", "PRIMAVERA", "HABIB JEWELS", "M.A.C", "ZARA", "BUBBLE LIFT", "TOP SHOP",
              "THE BODY SHOP", "CITY CHAIN", "TOMEI", "PDI", "ZARA MEN", "CHAMELEON", "HUSH PUPPIES", "ROMP",
              "DELIFRANCE", "ALI NOOR EXCHANGE", "MYNEWS.COM", "DR MOBILE CLINIC", "ROTIBOY"
              ]

shops_coor = {}

for i in range(len(start_point)):
    x = start_point[i]
    shops_coor[x] = shops_name[i]

concourse_level_routes = []
origin_to_destination = {}

print(len(start_point))
print(len(shops_name))
print(shops_coor)

global count_start
count_start = 0

draw_start(start_point)

global count_end
count_end = 1

draw_end(end_point)

# ----------------------------- Drawing walls/maze -----------------------------------------
WALLS = 2
global count_wall
count_wall = 0
wall = []
wall_record = []  # To record wall drawings

file1 = open("concourse_level", "rb")

for i in range(WALLS):
    wall.append([])

wall[0] = []
wall[1] = np.load(file1)

draw_wall(wall)

clock = pygame.time.Clock()

# ------------------------- Main Program Loop Start ---------------------------------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            # data = {'mall': {'name': 'KLCC', 'shop_list': {'from': 'LYSHA FLORA', 'to': 'KFC', 'path': shortest_path}}}
            # with open(f'sample_json.txt', 'w') as outfile:
            #     json.dump(data, outfile, indent=4)

            # file = open("saved_wall_2", "wb")
            # np.save(file, wall_record)
            # file.close()
            # print(concourse_level_routes)
            concourse_level_routes.append(origin_to_destination)
            data = {"mall": [{'name': 'KLCC', 'nav_list': concourse_level_routes}]}
            with open(f'all_routes.txt', 'w') as outfile:
                json.dump(data, outfile, indent=4)

            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # TODO: Add a JSON export function for the 'Export Path' button.
            # ----------------------- Clicking the 'Wall' button --------------------------------
            if Wall.isOver(pos):
                if count_wall < WALLS:
                    count_wall += 1

                    if count_wall == WALLS:
                        count_wall = 0

                        print(f"Start {count_start + 1}, End {count_end + 1}, Wall {count_wall + 1}")

                        grid_blank(grid)

                        image = pygame.image.load("suriaconcoursemap.png")
                        window.blit(image, [0, 0])

                        draw_wall(wall)
                        draw_start(start_point)
                        draw_end(end_point)

                    else:
                        print(f"Start {count_start + 1}, End {count_end + 1}, Wall {count_wall + 1}")

                        grid_blank(grid)

                        image = pygame.image.load("suriaconcoursemap.png")
                        window.blit(image, [0, 0])

                        draw_wall(wall)
                        draw_start(start_point)
                        draw_end(end_point)

            # ----------------------------- Clicking the 'Start Point' button -------------------------------------
            if Start.isOver(pos):
                if count_start < len(start_point):
                    count_start += 1

                    if count_start == len(start_point):
                        count_start = 0

                        print(f"Start {count_start + 1}, End {count_end + 1}, Wall {count_wall + 1}")

                        grid_blank(grid)

                        image = pygame.image.load("suriaconcoursemap.png")
                        window.blit(image, [0, 0])

                        draw_wall(wall)
                        draw_start(start_point)
                        draw_end(end_point)

                    else:
                        print(f"Start {count_start + 1}, End {count_end + 1}, Wall {count_wall + 1}")

                        grid_blank(grid)

                        image = pygame.image.load("suriaconcoursemap.png")
                        window.blit(image, [0, 0])

                        draw_wall(wall)
                        draw_start(start_point)
                        draw_end(end_point)

            # ------------------------- Clicking the 'End Point' button ----------------------------------------------
            if End.isOver(pos):
                if count_end < len(end_point):
                    count_end += 1

                    if count_end == len(end_point):
                        count_end = 0

                        print(f"Start {count_start + 1}, End {count_end + 1}, Wall {count_wall + 1}")

                        grid_blank(grid)

                        image = pygame.image.load("suriaconcoursemap.png")
                        window.blit(image, [0, 0])

                        draw_wall(wall)
                        draw_start(start_point)
                        draw_end(end_point)

                    else:
                        print(f"Start {count_start + 1}, End {count_end + 1}, Wall {count_wall + 1}")

                        grid_blank(grid)

                        image = pygame.image.load("suriaconcoursemap.png")
                        window.blit(image, [0, 0])

                        draw_wall(wall)
                        draw_start(start_point)
                        draw_end(end_point)

            # ------------------------- Clicking 'Clear' button -----------------------------------------------------
            if Clear.isOver(pos):
                # for row in range(ROWS):
                #     for column in range(COLUMNS):
                #         if (row, column) != selected_start and (row, column) != selected_end:
                #             grid[row][column].update(nodetype='blank', is_visited=False, is_path=False)
                #
                # image = pygame.image.load("suriaconcoursemap.png")
                # window.blit(image, [0, 0])
                #
                # draw_wall(wall)
                # draw_start(start_point)
                # draw_end(end_point)

                for i in range(2):
                    # i = count_start
                    selected_start = start_point[i]
                    for j in range(len(end_point)):
                        print(j)
                        if j == i:
                            pass
                        else:
                            count_end = j
                            selected_end = end_point[count_end]
                            print(selected_end)
                            # print(dijkstra(grid, start_point[i], end_point[j]))
                            origin_to_destination[f'{shops_coor[start_point[i]]} to {shops_coor[end_point[j]]}'] = dijkstra(grid, selected_start, selected_end)
                            print(origin_to_destination)

            # ------------------------- Clicking the 'Find' button --------------------------------------------------
            if Find.isOver(pos):
                dijkstra(grid, selected_start, selected_end)

            # ------------------------- Drawing the wall manually using the cursors ----------------------------------
            # TODO: Add 'erase wall' function
            if pos[1] <= SCREEN_HEIGHT - 1 and pos[0] <= SCREEN_WIDTH - 1:
                # Change the x/y screen coordinates to grid coordinates
                column_draw = pos[0] // (GRID_WIDTH)
                row_draw = pos[1] // (GRID_HEIGHT)
                coor = [row_draw, column_draw]
                wall_record.append(coor)

                grid[row_draw][column_draw].update(nodetype='wall')

                draw_square(row_draw, column_draw, WALL_COLOUR)
                pygame.display.flip()

                print(f"Wall drawn = {wall_record}")


    # ------------------------- Main Program Loop End -----------------------------------

    # ----------------------------- Dijkstra with A* extension algorithm --------------------
    def get_neighbours(node, max_length=ROWS - 1, max_width=COLUMNS - 1, diagonals=False):
        if not diagonals:
            neighbours = (
                ((min(max_length, node[0] + 1), node[1]), "+"),
                ((max(0, node[0] - 1), node[1]), "+"),
                ((node[0], min(max_width, node[1] + 1)), "+"),
                ((node[0], max(0, node[1] - 1)), "+")
            )
        else:
            neighbours = (
                ((min(max_length, node[0] + 1), node[1]), "+"),
                ((max(0, node[0] - 1), node[1]), "+"),
                ((node[0], min(max_width, node[1] + 1)), "+"),
                ((node[0], max(0, node[1] - 1)), "+"),
                ((min(max_length, node[0] + 1), min(max_width, node[1] + 1)), "x"),
                ((min(max_length, node[0] + 1), max(0, node[1] - 1)), "x"),
                ((max(0, node[0] - 1), min(max_width, node[1] + 1)), "x"),
                ((max(0, node[0] - 1), max(0, node[1] - 1)), "x")
            )
        # for neighbour in neighbours:
        #    if neighbour[0] != node:
        #        return neighbour

        return neighbours
        # return (neighbour for neighbour in neighbours if neighbour[0] != node)


    # -------------------------------------------------------------------------------------------------------------

    def neighbours_loop(
            neighbour,
            grid,
            visited_nodes,
            unvisited_nodes,
            queue,
            current_distance,
            astar=ASTAR
    ):
        neighbour_c, ntype = neighbour
        h_heuristic = 0

        if astar:
            # print("A* selected.")
            h_heuristic += abs(selected_end[0] - neighbour_c[0]) + abs(selected_end[1] - neighbour_c[1])
            h_heuristic *= 1

        if neighbour_c in visited_nodes:
            pass

        elif grid[neighbour_c[0]][neighbour_c[1]].nodetype == 'wall':
            visited_nodes.add(neighbour_c)
            unvisited_nodes.discard(neighbour_c)

        else:
            modifier = grid[neighbour_c[0]][neighbour_c[1]].distance_modifier

            if ntype == "+":
                heapq.heappush(queue, (current_distance + h_heuristic + 1 * modifier,
                                       current_distance + 1 * modifier,
                                       neighbour_c
                                       )
                               )

            elif ntype == "x":
                heapq.heappush(queue, (current_distance + h_heuristic + (2 ** 0.5) * modifier,
                                       current_distance + (2 ** 0.5) * modifier,
                                       neighbour_c
                                       )
                               )


    # -------------------------------------------------------------------------------------------------------------

    def traceback(selected_end, selected_start, v_distances, visited_nodes, grid_length,
                  grid, diags=DIAGONALS, visualise=VISUALISE):

        shortest_path = []
        path = [selected_end]
        shortest_path.append(list(selected_end))

        current_node = selected_end

        while current_node != selected_start:
            neighbour_distances = []
            neighbours = get_neighbours(current_node)

            # print(f"(Node): Distance = {v_distances}")

            for neighbour, ntype in neighbours:
                if neighbour in v_distances:
                    distance = v_distances[neighbour]
                    heapq.heappush(neighbour_distances, (distance, neighbour))
            # print(f"neighbour_distances = {neighbour_distances}")

            distance, smallest_neighbour = heapq.heappop(neighbour_distances)
            grid[smallest_neighbour[0]][smallest_neighbour[1]].update(is_path=True)

            if smallest_neighbour != selected_start:
                draw_square(smallest_neighbour[0], smallest_neighbour[1], PATH_COLOUR)
            else:
                pass

            path.append(smallest_neighbour)
            # print(f"path = {path}")
            shortest_path.insert(0, list(smallest_neighbour))
            # print(f"shortest_path = {shortest_path}")
            current_node = smallest_neighbour

            pygame.display.flip()
            grid[selected_start[0]][selected_start[1]].update(is_path=True)

        return shortest_path


    # --------------------------------------------------------------------------------------------------------

    # -------------------------- Dijkstra + A* algorithm -----------------------------------------------------
    def dijkstra(grid, selected_start, selected_end, visualise=VISUALISE, diagonals=DIAGONALS, astar=ASTAR):
        h_heuristic = 0
        g_distance = 0
        f_value = g_distance + h_heuristic

        grid_length = len(grid) - 1

        visited_nodes = set()
        unvisited_nodes = set([(x, y) for x in range(grid_length + 1) for y in range(grid_length + 1)])

        queue = []

        heapq.heappush(queue, (f_value, g_distance, selected_start))
        v_distances = {}
        priority, current_distance, current_node = heapq.heappop(queue)

        start = time.perf_counter()

        # ---------------- Main algorithm loop ------------------------------------------------
        while current_node != selected_end and len(unvisited_nodes) > 0:

            if current_node in visited_nodes:
                if len(queue) == 0:
                    return False
                else:
                    priority, current_distance, current_node = heapq.heappop(queue)
                    continue

            for neighbour in get_neighbours(current_node):
                neighbours_loop(
                    neighbour,
                    grid,
                    visited_nodes,
                    unvisited_nodes,
                    queue,
                    current_distance,
                )

            visited_nodes.add(current_node)
            unvisited_nodes.discard(current_node)

            v_distances[current_node] = current_distance
            # print(v_distances)

            if current_node != selected_start:
                grid[current_node[0]][current_node[1]].update(is_visited=True)
                draw_square(current_node[0], current_node[1], SCAN_COLOUR)
                pygame.display.flip()

                if VISUALISE:
                    update_square(current_node[0], current_node[1])
                    time.sleep(0.000001)

            if len(queue) == 0:
                return False
            else:
                priority, current_distance, current_node = heapq.heappop(queue)

        v_distances[selected_end] = current_distance + (1 if not diagonals else 2 ** 0.5)
        visited_nodes.add(selected_end)

        pathz = traceback(selected_end, selected_start, v_distances, visited_nodes, grid_length, grid)

        end = time.perf_counter()
        num_visited = len(visited_nodes)
        time_taken = end - start

        # print(
        #     f"Program finished in {time_taken:.4f} seconds after checking {num_visited} nodes."
        #     f"That is {time_taken / num_visited:.8f} seconds per node."
        # )
        return pathz
        return False if v_distances[selected_end] == float('inf') else True
