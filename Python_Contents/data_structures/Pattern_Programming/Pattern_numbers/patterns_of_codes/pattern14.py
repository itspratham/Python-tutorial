n=10
for i in range(n):
    if i%2==0:
        s=0
        s1=1
    else:
        s1=0
        s=1
    for j in range(i):
        if j%2==0:
            print(s,end=" ")
        else:
            print(s1,end=" ")
    print(" ")

