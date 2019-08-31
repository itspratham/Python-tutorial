r=7
count=1
for i in range(1,10):
    for j in range(i+r):
        print(end=" ")
    for d in range(1,i):
        print(count,end=" ")
        count=count+1
    print()
    r = r-2


