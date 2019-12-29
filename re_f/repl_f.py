import re
str_1 = "12dd44gg55"

def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

print(re.sub("(?P<value>\d+)", double, str_1))
