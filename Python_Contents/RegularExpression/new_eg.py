import re

a = "123abc"
t = re.match("[a-z]+", a)
q = re.search("[a-z]+", a)

print(t)
print(q)
