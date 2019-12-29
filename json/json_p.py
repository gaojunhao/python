import json

dict_1 = {'s':1, 'd':2}

json_str = json.dumps(dict_1)

print(dict_1)

print(json_str)

dict_2 = json.loads(json_str)
print(dict_2)
