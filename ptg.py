# largest subsequent 1s in a  binary array
# [1,0,0,1,1,1]


# def decorator_fun(func):
#     def inner_func(*args, **kwargs):
#         print("hello1")
#         func(*args, **kwargs)
#     return inner_func
#
# @decorator_fun
# def a_func():
#     print("hello")
#
# a_func()


def next_permutation(data, i, length, arr):
    if i == length:
        print(data)
        return

    for j in range(i, length):
        data[i], data[j] = data[j], data[i]
        next_permutation(data, i + 1, length, arr)
        data[i], data[j] = data[j], data[i]


print(next_permutation([1, 2, 3, 6, 5, 4], 0, 6, []))
