'''
string can't be changed
'''
str_1 = 'string1'

str_2 = 'string2'

int_1 = 10
print(str_1, str_2);

print("my name is %s, age is %d\n" % (str_1, int_1))

print(f'Hello {str_2}')

print(str_1.capitalize());

str_3 = 'sdfsdfg'

print(str_3.count('s',0,len(str_3)))

if str_3.find('s',0,len(str_3)) != -1:
    print(True)
else:
    print(False)
str_4 = ' '
print(str_4.join('sgfsd'))

str_5 = 'DFKsdH'

print(str_5.lower())

print(str_5.replace('d','A'))

str_6 = 'dds  '
print(str_6, str_6.rstrip())

str_7 = 'dfgfhgk'
print(str_7.split('f',str_7.count('f')))
