sort = input("Enter the numbers: ").split()


def insertion_sort(sort):
    sort = list(map(int, sort))
    for i in range(0, len(sort)):
        for j in range(0, len(sort)-1):
            if sort[i] > sort[j]:
                sort[i], sort[j + 1] = sort[j + 1], sort[i]
    x = list(sort)
    return x


print(insertion_sort(sort))
