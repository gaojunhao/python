def f1(a, b = 2, c = 4):
    print("a: %d" %(a), b, c)

f1(3,5,c = 6)

def tuple_v(args, *vtuple):
    print(args)
    print(vtuple)
    for x in vtuple:
        print(x)

def dict_v(args, **vdict):
    print(args)
    print(vdict)

tuple_v(1,'s',2,"ddd")

dict_v('s', a = {'s':1,4:2}, d = ('c','d',1))

# python3.8 support
#def f2(a,b,/,d,*,c):
#    print(a,b,c,d)
#
#f2(1,2,10,c=98)
