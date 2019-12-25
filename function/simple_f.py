def hello(a,b):
    return a * b
a,b = map(int,input("input a,b \n").split())
print("hello(%d,%d) = %d" %(a, b, hello(a,b)))
