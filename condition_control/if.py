value_str = input("input a number from 1 to 10\n")
value = int(value_str)
if value in range(1,6):
    print("value %d in 1-5" %(value))
elif value in range(6,11):
    print("value %d in 6-10" %(value))
else:
    print("value %d is not in 1-10" %(value))
