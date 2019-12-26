dict_1 = dict([('a',1),('b',2),('c',3)])
print(dict_1)

dict_2 = {x:y for x in range(3) for y in set('abc')}
print(dict_2)

print(dict(a=1,b=2,c=3))
