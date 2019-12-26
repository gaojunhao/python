var = [1, 3, 4]
print([v*2 for v in var if v > 3])

var_1 = ['a', 'b', 'c']
var_2 = [1, 2, 3, 4]
print([var_1[i]+str(var_2[j]) for i in range(len(var_1)) for j in range(len(var_2))])
