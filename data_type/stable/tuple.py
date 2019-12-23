'''
tuple is like list
difference between tuple and list
element of tuple can't be changed
but list can be changed
'''

tuple = ('c', 2, 'df', 3.92)

print(tuple)

tuple_1 = (1,)
print(type(tuple_1))

tuple_2 = (2,'f')
print(type(tuple_2))

tuple_3 = (2, 3)
print(type(tuple_3))

tuple_4 = (tuple_2, tuple_3)
for x in tuple_4:
    print(x)
