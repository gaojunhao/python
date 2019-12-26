set_1 = set('123445')
print(set_1)
set_2 = set('22335')
print(set_1 - set_2)

print({x for x in set('1223445') if x not in set('12')})
