'''
dictionary is a mapping type of key:value
'''

dict = {}
dict['one'] = 1
dict[2] = 'two'

tinydict = {'name':'tom', 'age':1}
print(dict[2], tinydict['age'])

print(len(dict))

print(dict.get('one'))

if 'one' in dict:
    print(True)
else:
    print(False)

print(list(dict.keys()))
