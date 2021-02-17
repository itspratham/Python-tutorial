"""
    1       1
     2     2
      3   3
       4 4
        5
       4 4
      3   3
     2     2
    1       1
"""

h = 1
r = 3
u = 2
s = 1
for i in range(1, 5):
    for j in range(i):
        print(" ", end=" ")
    for k in range(1):
        print(h, end=" ")
    for j in range(i + r):
        print(" ", end=" ")
    for j in range(i + u):
        print(" ", end=" ")
    for g in range(1):
        print(s, end=" ")
    s = s + 1

    r = r - 2
    u = u - 2

    h = h + 1

    print(" ")
r = 4
k = 5
s = 5
for i in range(1, 6):
    for j in range(i + r):
        print(" ", end=" ")

    for h in range(1):
        print(k, end=" ")
    for j in range(i - 1):
        print(" ", end=" ")
    for j in range(i - 2):
        print(" ", end=" ")
    if i > 1:
        print(s, end=" ")

    r = r - 2
    s = s - 1
    k = k - 1

    print(" ")
