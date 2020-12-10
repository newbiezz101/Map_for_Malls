import json

path = [[1, 2], [2, 3], [3, 4]]

data = {"mall": {"klcc": {"route": path}}}

data2 = {'mall': [{'name':'KLCC','shop_list': [{'Source': 'kinokuya', 'Destination': 'kfc', 'Path': path}]}]}

i = 1
with open(f'json{1}.txt', 'w') as outfile:
    json.dump(data2, outfile, indent=4)
