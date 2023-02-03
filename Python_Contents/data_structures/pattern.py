#         1
#       1   1
#     1   2   1
#   1   3   3   1
# 1   4   6   4   1

g = 6
for i in range(0, 6):
    for k in range(i):
        print("*", end="$")
    print(" ")
