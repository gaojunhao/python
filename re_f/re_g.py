import re
str_1 = 'cat is smarter than dog'

print(re.search('is', str_1).span())
it = re.finditer('\w+', str_1)
for match in it:
    print(match.group())
print(re.search('is', str_1).start())
print(re.search('is', str_1).end())
