multi_list = [[1,2,3,4],[5,6,7,8],[9,10,11,12],]
print([[row[i] for row in multi_list] for i in range(4)])

list_1 = [1, 2, 3, 4]
del list_1[1:3]
print(list_1)
del list_1[:]
print(list_1)
