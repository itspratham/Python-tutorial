def intersection(n1, n2):
    l = []
    for i in range(len(n1)):
        if n1[i] in n2:
            l.append(n1[i])
    return l


print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
