'''
list is like string
difference between list and string
element of string can't be changed,
but list can be changed
'''

list_3 = [1, 'a', 'ab', 1+2j]

list_3[1] = 'c'

list_3[2] = 4

del list_3[3]

list_1 = [2, 3, 4]

print(list_3 + list_1)

print(len(list_3))

for x in list_3:
    print(x)

list_2 = [list_3, list_1]

print(list_2[0][1])

list_3[0] = 2
list_1[0] = 3 
for x in list_2:
    print("list_2" + str(x))

tuple = (1, 'c', 1+9j)
print(list(tuple))
