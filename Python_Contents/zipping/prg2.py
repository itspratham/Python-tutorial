def bs(a):
    # a = name of list
    b = len(a) - 1
    # minus 1 because we always compare 2 adjacent values
    for x in range(b):
        for y in range(b - x):
            a[y] = a[y + 1]
    return a


a = [32, 5, 3, 6, 7, 54, 87]
print(bs(a))
