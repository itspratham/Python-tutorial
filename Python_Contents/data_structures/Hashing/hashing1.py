# # Naive method to find a pair in a list with given sum
#
# def findPair(arr, summ):
#     dictionary = {}
#     for i, e in enumerate(arr):
#         if summ-e in dictionary:
#             print("Pair found at index", dictionary.get(summ - e), "and", i)
#             return
#         dictionary[e] = i
#     print("Pair not found")
#
# findPair([8, 7, 2, 5, 3, 1], 10)
#
#

# Find four elements a, b, c and d in an array such that a+b = c+d
# def sum__(arr):
#     HASH = {}
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             summ = arr[i] + arr[j]
#             if summ in HASH.keys():
#                 prev = HASH.get(summ)
#                 print(str(prev), "and ({}, {})".format(arr[i], arr[j]))
#                 return
#             else:
#                 HASH[summ] = (arr[i], arr[j])
#     print(HASH)
#     return "Not Found"
#
# sum__([3, 4, 7, 1, 2, 9, 8])


# Count distinct elements in every window of size k

# Input: arr[] = {1, 2, 1, 3, 4, 2, 3};
#        k = 4
# Output: 3 4 4 3
#
# Explanation:
# First window is {1, 2, 1, 3}, count of distinct numbers is 3
# Second window is {2, 1, 3, 4} count of distinct numbers is 4
# Third window is {1, 3, 4, 2} count of distinct numbers is 4
# Fourth window is {3, 4, 2, 3} count of distinct numbers is 3
#
# Input: arr[] = {1, 2, 4, 4};
#        k = 2
# Output: 2 2 1
#
# Explanation:
# First window is {1, 2}, count of distinct numbers is 2
# First window is {2, 4}, count of distinct numbers is 2
# First window is {4, 4}, count of distinct numbers is 1

# def windows(arr):
#
