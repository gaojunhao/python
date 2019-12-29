import re
str = "cat is smater than dog"

#match is start from beginning
matchobj = re.match("dog", str, re.M|re.I)

if matchobj:
    print("match is true\n")
else:
    print("match is false\n")

#search is scan overall sentence
searchobj = re.search("dog", str, re.M|re.I)

if searchobj:
    print("search is true\n")
else:
    print("search is false\n")
