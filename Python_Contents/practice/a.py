import re

with open("ggg.py", "r") as r:
    f = r.read()
    for i in f.split("\n"):
        if re.match(r".*error.*", i):
            print(i)
