ROWS = 2
COLUMNS = 3

grid = []

for row in range(COLUMNS):
    grid.append([])
    for column in range(COLUMNS):
        grid[row].append(1)

grid[0][1] = 2

maze = []
wall = []

WALLS = 3

for i in range(WALLS):
    wall.append([])

wall[0] = [[1, 2], [2, 3], [3, 4]]
wall[1] = [[2, 3], [3, 4], [4, 5], [5, 6]]
wall[2] = [[6, 7], [7, 8]]

for i in range(WALLS):
    maze.append(wall[i - 1])

print(maze)
# print(grid[0])
# print(grid)
