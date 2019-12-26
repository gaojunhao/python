print('{1}-->{0}' .format('s','n'))

print('{a}-->{b}' .format(b=2,a=1))

print('{0:10}-->{1:10}' .format('qa',2))

tuple_1 = ('a',2)
tuple_2 = ('b',3)
dict_1 = dict([tuple_1,tuple_2])
print(dict_1)
print('a: {0[a]:d}; b: {0[b]:d}' .format(dict_1))
