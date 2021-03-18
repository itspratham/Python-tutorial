n = 100
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n:
            print(j, end=" ")
        elif j == n - i + 1:
            print(n - i + 1, end=" ")
        else:
            print(" ", end=" ")
    print()
