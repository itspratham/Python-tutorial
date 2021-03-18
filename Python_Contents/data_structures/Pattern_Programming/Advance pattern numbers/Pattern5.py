r = 7
d = 6

for i in range(1, 8):
    for j in range(i + r):
        print("*", end="")

    for k in range(1, i + 1):
        print(str(i) + "*", end="")

    for j in range(i + d):
        print("*", end="")
    r = r - 2
    d = d - 2
    print()
