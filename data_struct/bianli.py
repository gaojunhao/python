#items
dict_1 = dict([('a',1),('b',2),('c',3)])
for x,y in dict_1.items():
    print(x+':',str(y))

#enumerate
list_1 = [1,2,3]
for x,y in enumerate(list_1):
    print(x,':',y)

#zip, format
list_2 = ['name1', 'name2', 'name3']
list_3 = ['a', 'b', 'c']
for x,y in zip(list_2, list_3):
    print("{0} is {1}" .format(x, y))

#reversed
for x in reversed([1,2,3]):
    print(x)

#sorted
for x in sorted([4,5,6]):
    print(x)
