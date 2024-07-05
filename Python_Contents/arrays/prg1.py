# Write a Python program to create an array
# of 5 integers and display the array items.
# Access individual element through indexes.


# array_num = array('i', [1,3,5,7,9])
# for i in array_num:
#     print(i)
# print("Access first three items individually")
# print(array_num[0])
# print(array_num[1])
# print(array_num[2])

# Write a Python program to append a new item to the end of the array.
# array_num = array('i', [1,3,5,7,9])
# array_num.append(7)
# print(array_num)

# Write a Python program to reverse the order of the items in the array.
# array_num = array('i', [1,3,5,7,9])
# array_num.reverse()
# print(array_num)

# Write a Python program to get the length in bytes of one array item in the internal representation.
# array_num = array('i', [1,3,5,7,9])
# print(array_num.itemsize)

# Write a Python program to get the current memory address and the length in
# elements of the buffer used to hold an arrays
# contents and also find the size of the memory buffer in bytes.

# array_num = array('i', [1,3,5,7,9])
# print(array_num.buffer_info())
# print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))


# Find the largest number in the array
# def find_the_largest(arr):
#     maximum_no = arr[0]
#     second_max = arr[0]
#     for i in arr:
#         if i > maximum_no:
#             second_max = maximum_no
#             maximum_no = i
#         elif i > second_max and i != maximum_no:
#             second_max = i
#     return second_max
#
#
# print(find_the_largest([3, 4, 2, 6, 7, 0, 1, 9, 10, 11]))


# def perm1(lst):
#     if len(lst) == 0:
#         return []
#     elif len(lst) == 1:
#         return [lst]
#     else:
#         l = []
#         for i in range(len(lst)):
#             x = lst[i]
#             # print(x)
#             xs = lst[:i] + lst[i + 1:]
#             # print(xs)
#             for p in perm1(xs):
#                 l.append([x] + p)
#         return l
#
#
# print(perm1(["a", "b", "c"]))

# def get_permutation(string, i=0):
#     if i == len(string):
#         print("".join(string))
#
#     for j in range(i, len(string)):
#
#         words = [c for c in string]
#         print(words)
#         # swap
#         words[i], words[j] = words[j], words[i]
#
#         get_permutation(words, i + 1)
#
#     return ""
#
#
# print(get_permutation('abc'))
#
# # Function to swap two characters in a character array
# def swap(ch, i, j):
#     temp = ch[i]
#     ch[i] = ch[j]
#     ch[j] = temp


# Recursive function to generate all permutations of a string
# def permutations(ch, curr_index=0):
#     if curr_index == len(ch) - 1:
#         print(''.join(ch))
#
#     for i in range(curr_index, len(ch)):
#         swap(ch, curr_index, i)
#         permutations(ch, curr_index + 1)
#         swap(ch, curr_index, i)
#
#
# if __name__ == '__main__':
#     s = 'ABC'
#     permutations(list(s))


# def get_per(string, i):
#     if i == len(string):
#         print(string)


# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return "Found"
#         elif arr[mid] > target:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return
#
#
# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 1))

# def transform(a = 2):
#     if a == 1:
#         return a +- 2
#     return a
#
# total = 1
#
# for x in [3,5,1]:
#     total = total + transform(x)
#
# print(total)

# class Square:
#
#     def Area(self, side):  # definiting method with 1 argument
#
#         return side * side
#
#
# class Rectangle(Square):
#
#     def Area(self, length, bredth):  # overriding method with 2 arguments
#
#         return length * bredth
#
#
# f = Rectangle()
# print(f.Area(3, 4))

# Given an integer array,
# find the contiguous subarray
# (containing at least one number) which has the largest
# sum and return its sum? (solution)
f = [-2, -3, 4, -1, -2, 1, 5, -3]

# iterate over the array if sum <0, consider the sum from the current element
#

# def find_sum(arr):
