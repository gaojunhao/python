f = open('./print.py', 'r')
print(f.read())
f.close()

with open('./print.py', 'r') as f:
    for line in f:
        print(line)
