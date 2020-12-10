import numpy as np

wall = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]

file = open("saved_wall", "wb")
np.save(file, wall)
file. close
