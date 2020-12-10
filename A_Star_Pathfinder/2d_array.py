ROWS = 2
COLUMNS = 3

grid = []

for row in range(COLUMNS):
    grid.append([])
    for column in range(COLUMNS):
        grid[row].append(1)

grid[0][1] = 2

print(grid[0])
print(grid)