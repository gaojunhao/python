'''
set is used for set comparison
'''

set_1 = {'a', 1, 'df'}
set_2 = set('a1df')

print(set_1)

print(set_2)

print(set_1 - set_2)

set_1 = set((34, 1+9j, 'a'))
print(set_1)
set_1.update([2, 4])
set_1.add("gf")
set_1.update({'d':89})
print(set_1)

set_1.remove('d')
print(set_1)

set_1.pop()
print(set_1)
