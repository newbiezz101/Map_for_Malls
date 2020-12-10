import numpy as np

file1 = open("saved_wall_1", "rb")
file2 = open("saved_wall_2", "rb")

npwall1 = np.load(file1)
npwall2 = np.load(file2)

wall1 = npwall1.tolist()
wall2 = npwall2.tolist()
#wall3 = wall2.extend(wall1)
wall3 = wall1 + wall2

erase_wall = [[14, 75], [14, 75], [36, 115], [32, 97], [20, 51], [44, 72]]
add_wall = [[44, 57], [43, 57], [42, 57], [41, 57], [40, 57], [40, 56], [40, 55], [40, 54], [43, 73], [42, 73],
            [41, 73], [40, 73], [40, 74], [40, 75], [40, 76], [26, 55], [27, 55], [28, 55], [29, 55], [29, 76],
            [29, 75]]

for erase_point in erase_wall:
    wall3.remove(erase_point)

for add_point in add_wall:
    wall3.append(add_point)
# wall3.remove([14, 75])
# wall3.remove([44, 72])
# wall3.remove([36, 115])
# wall3.remove([32, 97])
# wall3.remove([20, 51])
print(type(wall1))
print(type(wall2))
print(wall3)

file = open("saved_wall_3", "wb")
np.save(file, wall3)
file.close

# file4 = open("concourse_level", "wb")
# np.save(file4, wall3)
# file4.close