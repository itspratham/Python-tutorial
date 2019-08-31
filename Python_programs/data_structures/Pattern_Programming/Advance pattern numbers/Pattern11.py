r=6
f=1
ch=65
d=1
n=4
for i in range(7):
    for j in range(i+r):
        print(" ",end=" ")

    for k in range(i+f):
        print(chr(ch),end=" ")
        ch = ch + 1

    for g in range(i+f):
        print(d,end=" ")
        d=d+1
    print()
    r=r-2
    ch=65
    d=1
