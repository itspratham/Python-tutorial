import re

# Difference between match and search
line = "Cats are smarter than dogs"
matchObj = re.match(r'dogs', line, re.M|re.I)

if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

searchObj = re.search(r'dogs', line, re.M|re.I)
if searchObj:
    print("Search --> searchObj.group() : ", searchObj.group())
else:
    print("No match!!")