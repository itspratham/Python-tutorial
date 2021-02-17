g = 0
temp = 0
n = 30
for i in range(n):
    for j in range(i + 1):
        print(g * i, end=" ")
        g = g + 1
    print(" ")
    g = temp
