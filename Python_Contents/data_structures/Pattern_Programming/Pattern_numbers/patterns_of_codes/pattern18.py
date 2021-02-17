n = 10
for i in range(1, n):
    for j in range(i):
        print(i, end=" ")
        i = i - 1
    print(" ")
