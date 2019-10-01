k=6
for i in range(1,8):
    for j in range(1,i):
        print("*",end=" ")
    # for h in range(1):
    #     print(" ",end=" ")
    for j in range(k):
        print("#",end=" ")
    k=k-1

    print()