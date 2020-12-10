grid = []

ROWS = 40
COLUMNS = 40

for row in range(ROWS):
    grid.append([])
    for column in range(COLUMNS):
        grid[row].append(1)

print(grid)

start = (30, 2)

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
    #for neighbour in neighbours:
    #    if neighbour[0] != node:
    #        return neighbour
    return neighbours
    #return (neighbour for neighbour in neighbours if neighbour[0] != node)


#for neighbour in get_neighbours(start):
print(get_neighbours(start)[0][0])
