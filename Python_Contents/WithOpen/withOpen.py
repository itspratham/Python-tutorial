# Context managers
"""
with open("Student Name.txt" ,"r") as fo:
    for line in fo.readlines():
        print(line)
"""

s= """Let's go over what we have. Like any class, there's an __init__() 
method that sets up the object (in our case, setting the file name to open 
and the mode to open it in). __enter__() opens and returns the file 
(also creating an attribute"""




with open("poem.txt", "w") as fo:
    fo.write(s)


with open("poem.txt", "r") as fo:
    print(fo.readlines())


