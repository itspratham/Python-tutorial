# def func(x, li):
#     a = 5
#     if x < 0:
#         print(x)
#         li.append(x)
#         li = li + li[-2::-1]
#         return li
#     li.append(x)
#
#     return func(x - a, li)
#
#
# print(func(16, []))

# Function to find permutations of a given string
from itertools import permutations


def allPermutations(str):
    # Get all permutations of string 'ABC'
    permList = permutations(str)
    print(list(permList))
    # print all permutations
    for perm in list(permList):
        print(''.join(perm))


# Driver program
if __name__ == "__main__":
    str = 'ABC'
    allPermutations(str)
