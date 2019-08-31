g=1
r=3
for i in range(1,6):
    if i<=6:
        print(i,end=" ")
        i=i+1
    for j in range(i+r)  :
       print("*",end=" ")
       r=r-1
    print( )
