r = 7
h = 8
k = 1
for i in range(1, 9):
    for j in range(i + r):
        if i % 2 != 0:
            print(h, end=" ")
            h = h - 1

        else:
            print(k, end=" ")
            k = k + 1
    print(" ")
    r = r - 2
    h = 8
