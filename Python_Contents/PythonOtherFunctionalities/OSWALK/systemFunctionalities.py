import os
from os.path import join, getsize

# in OS Namespace
# os.path.join()
# Local Namespacew
# join()

# Create a Directory
# os.system("md mydir")
# os.system("rmdir mydir")

# OS. walk
for root, dir, file in os.walk("E:\ProgramData"):
    # print(root)
    # print (dir)
    # print (file)
    if os.path.isdir(os.path.join(root)):
        print("Yes")
    else:
        print("No")
    print(dir)
    print([os.path.join(root, name) for name in file])
    print("{} kb".format(sum([getsize(join(root, name)) for name in file])))

# Is file or not

file = "C:\Python35\Lib\msilib\schema.py"

if os.path.isdir(file):
    print("Yes its DIR")
elif os.path.isfile(file):
    print("Yes its file")
else:
    print("Error")
