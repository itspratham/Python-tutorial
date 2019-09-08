import re
regEx = re.compile('[Pp]ython')
line = regEx.search('I am learning python')
if line:
    print("Search --> searchObj.group() : ", line.group())
else:
    print("No match!!")

