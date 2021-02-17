g = 8
d = 9
for i in range(1, 10):
    for j in range(i + g):
        print(d, end=" ")
    print(" ")
    d = d - 1
    g = g - 2
