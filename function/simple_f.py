def hello(a,b):
    return a * b
a,b = map(int,input("input a,b \n").split())
print("hello(%d,%d) = %d" %(a, b, hello(a,b)))

def immutable(a):
    a = 10
c = 11
print("before immutable a:%d" %(a))
immutable(c)
print("after immutable a:%d" %(a))

def mutable(list):
    list[1] = 2
list_1 = ['a', 3, 'b']
print("before mutable:", list_1)
mutable(list_1)
print("after mutable:", list_1)

list_2 = input("judge input value num\n").split()
print(len(list_2))
