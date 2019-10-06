v=7
for i in range(7):
    for j in range(i+1):
        print("*",end="")
    for h in range(i+v-1):
        print(" ",end="")
    for h in range(i+v+1):
        print("*",end="")
    for j in range(i):
        print(" ",end="")
    for j in range(i):
        print(" ",end="")
    for h in range(i+v):
        print("*",end="")
    for h in range(i+v-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    v = v - 2
    print()
