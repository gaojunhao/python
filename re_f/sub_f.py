import re
str = "11111 # nhnh"

str_1 = re.sub("#.*$", "", str)
print(str_1)

str_2 = re.sub("\D", "", str)
print(str_2)
