g=6
d=9
for i in range(1,8):
    for j in range(i+g):
        print(" ",end=" ")

    for k in range(i):
        print(i,end="   ")
    print(" ")
    d=d-1
    g=g-2