sort = input("Enter the numbers: ").split()


def insertion_sort(sort):
    sort = list(map(int, sort))
    flag = 0
    for i in range(0, len(sort)):
        for j in range(1, len(sort)):
            if sort[i] > sort[j]:
                sort[i], sort[j + 1] = sort[j], sort[j]
                flag = 1
        if flag == 0:
            print("vbrhf")
            break
    x = list(sort)
    return x


print(insertion_sort(sort))
