k=2
g=1
temp=1
temp1=2
for i in range(1,10):
    g = temp # initialize g to 1
    k=temp1  # initialize k to 2
    for j in range(i):
        if i%2==0:
            print(k,end=" ")
            k=k+2

        else:
             print(g,end=" ")
             g=g+2

    print(" ")