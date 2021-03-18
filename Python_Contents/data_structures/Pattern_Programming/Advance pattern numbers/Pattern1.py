n = 9
r = n + 9
d = n - 2
for i in range(1, n):
    for j in range(i + d):
        print(r, end=" ")
        r = r - 1
    print("")
    d = d - 2
