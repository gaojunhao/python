tuple_value = ('a', 1, 'b', 2)
x = 0
while x < 4:
    print("tuple[%d]:%s" %(x,str(tuple_value[x])))
    x = x + 1
else:
    print("value is larger than 4")
