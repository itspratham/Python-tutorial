# def permute(data, i, length):
#     if i == length:
#         print(''.join(data))
#     else:
#         for j in range(i, length):
#             # swap
#             data[i], data[j] = data[j], data[i]
#             print(data, "hello")
#             permute(data, i + 1, length)
#             data[i], data[j] = data[j], data[i]
#
# string = "ABC"
# n = len(string)
# data = list(string)
# permute(data, 0, n)


def permutation(data, i, length):
    if i == length:
        print(''.join(data))
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permutation(data, i + 1, length)
            data[i], data[j] = data[j], data[i]


permutation(list("ABCDEF"), 0, 6)
