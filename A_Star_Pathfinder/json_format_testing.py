import json
path = [[1, 2], [2, 3], [3, 4]]
shops = [(30, 2), (30, 4), (30, 6), (16, 56), (7, 60), (12, 74)]

shops_names = ["LYSHA FLORA", "MINT COBBLER", "FOTOPOINT", "KFC", "PRAYING ROOM", "MAYBANK"]

shops_coor = {}

routes = {}

for i in range(len(shops)):
    x = shops[i]
    shops_coor[x] = shops_names[i]
#test[path[1]] = shop[0]

klcc_routes = []
start = {}
origin_to_destination = {}

for i in range(len(shops)):
    for j in range(len(shops)):
        if j == i:
            pass
        else:
            origin_to_destination[f'{shops_coor[shops[i]]} to {shops_coor[shops[j]]}'] = path
            klcc_routes.append(origin_to_destination)
            #print(klcc_routes)

print(klcc_routes)

data = {"mall": [{'name': 'KLCC', 'nav_list': klcc_routes}]}
#
# data2 = {'mall': [{'name':'KLCC','shop_list': [{'Source': 'kinokuya', 'Destination': 'kfc', 'Path': path}]}]}
#
i = 1
with open(f'json{1}.txt', 'w') as outfile:
    json.dump(data, outfile, indent=4)