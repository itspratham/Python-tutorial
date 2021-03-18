# num = 7, no_of_lines = 4
# 7
# 14 15
# 28 29 30 31
# 56 57 58 59 60 61 62 63

no_of_lines = 4
num = 7
k = 0

for i in range(no_of_lines):
    g = 0
    for j in range(pow(2, k)):
        print(num + g, end=" ")
        g = g + 1
    k = k + 1
    num = num * 2
    print()
