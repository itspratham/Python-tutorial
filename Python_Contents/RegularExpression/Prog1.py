import re

line = "Cats dffd smarter than are dogs hello\n"
matchObj = re.match(r'(.*) are (.*)', line, re.I)
print(matchObj)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))

else:
    print("No match")
