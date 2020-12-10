import json
import jsonpickle

path = [[1,2],[2,3],[3,4]]

enpath = jsonpickle.encode(path)
jpath = json.dumps(enpath)

lpath = json.loads(jpath)
delpath = jsonpickle.decode(lpath)

print(type(path))
print(enpath)
print(jpath)
#print(depath)
print(type(lpath))
print(type(delpath))
#print(ttest)

