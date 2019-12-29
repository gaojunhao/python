import json

dict_1 = {'s':1, 'd':2}

json_str = json.dumps(dict_1)

with open('./data.json', 'w') as f:
    json.dump(json_str, f)

with open('./data.json','r') as f:
    print(json.load(f))
