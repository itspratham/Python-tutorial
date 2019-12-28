l = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# for _ in range(6):
#     l.append(list(map(int, input().rstrip().split())))

def rotate( l ):
    new_l = []
    b = 0
    for i in range(1, 4):
        temp= []
        a = 2
        for j in range(1, 4):
            temp.append( l[a][b] )
            a = a - 1

        new_l.append( temp )
        b = b + 1

    return new_l.copy()

l = rotate( l )

for i in range(len(l)):
    for j in range(len(l)):
        print(str(l[i][j]),end=" ")
    print()

print()
print()

l = rotate( l )

for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j],end=" ")
    print()

print()
print()

l = rotate( l )

for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j],end=" ")
    print()

print()
print()