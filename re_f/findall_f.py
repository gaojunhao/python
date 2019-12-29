import re

str_1 = 'jh7sffgusf78'

pattern = re.compile(r'\d+')
print(pattern.findall(str_1))

print(pattern.findall(str_1, 0, 5))


it = re.finditer(r'\d+', str_1)
for match in it:
    print(match.group())
