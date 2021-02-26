def func(x, li):
    a = 5
    if x < 0:
        print(x)
        li.append(x)
        li = li + li[-2::-1]
        return li
    li.append(x)

    return func(x - a, li)


print(func(16, []))
