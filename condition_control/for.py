dict_value = {'a':1, 2:7, (1,2):[3,4]}
for x in dict_value.keys():
    print(x,dict_value.get(x))
