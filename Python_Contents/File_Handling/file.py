# x=open("hen.txt","r")
# #print(x.read(7))
# print(x.readlines())

# f = open("hen.txt", "r")
# for x in f:
#   print(x)

# f = open("hen.txt", "a")
# f.write("Now the file has more content!")
# f.close()
#Assignment- Do it through loop

#
# f = open("hen.txt", "r")
# print(f.read())

# f = open("hen.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()


# f=open("hen1.txt","x")

# f=open("E:\Python\python programs\Python\FirstProject\dog.txt","a")
# f.write("hello How are you")



# import os
# os.remove("E:\Python\python programs\Python\FirstProject\dog.txt")




f = open("hen.txt","r")
filee = f.read()

fdf = filee.replace("'",'""')

g = open("hen.txt","w")
g.write(fdf)
