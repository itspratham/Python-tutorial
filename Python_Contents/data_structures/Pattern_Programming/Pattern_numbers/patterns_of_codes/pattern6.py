h = 8
com = 1
s = 1
for i in range(1, 6):
    for c in range(1, i):
        print(" ", end=" ")
    for j in range(i + h):
        print(com, end=" ")
        com = com + 1
    print(" ")
    h = h - 3
    com = s
