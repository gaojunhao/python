import re

print(re.split('\W+', 'ss, dd, gg.'))
print(re.split('\W+', 'ss, dd, gg.', 1))
print(re.split('(\W+)', 'ss, dd, gg.'))

