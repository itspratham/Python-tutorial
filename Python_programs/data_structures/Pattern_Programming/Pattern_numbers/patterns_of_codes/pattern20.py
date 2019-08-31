temp = 1
n=5
for i in range(1,n+1):
    temp=i
    for j in range(1,n+1):
        print(temp,end=" ")
        temp=temp+1
        if temp>=n+1:
            temp=1
    print(" ")
    temp=temp-2


