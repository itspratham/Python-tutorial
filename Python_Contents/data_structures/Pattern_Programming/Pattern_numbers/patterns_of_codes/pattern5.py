
k=6
for i in range(1,8):
    for j in range(i+k):
        print("#",end=" ")

    for f in range(1,i+1):
        print(f,end="   ")
    print(" ")
    k=k-2
