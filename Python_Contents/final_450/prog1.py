# Array	Reverse the array
# def reverse_array(arr):
#     start = 0
#     end = len(arr)-1
#     while start < end:
#         temp = arr[start]
#         arr[start] = arr[end]
#         arr[end] = temp
#         start = start+1
#         end = end-1
#     return arr
#
#
# print(reverse_array([4, 5, 1, 6, 7]))
import math


# Array	Find the maximum and minimum element in an array	

# def find_max_min(arr):
#     maxx = arr[0]
#     minn = arr[0]
#     for i in range(len(arr)):
#         if arr[i] > maxx:
#             maxx = arr[i]
#         if arr[i] < minn:
#             minn = arr[i]
#     return maxx, minn
# print(find_max_min([1,5,9,4,7]))


# Array	Find the "Kth" max and min element of an array
# def array_(arr, k):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr[k], arr[len(arr)-k]
#
# print(array_([4,1,6,8,4], 2))


# Array	Given an array which consists of only 0, 1 and 2.
# Sort the array without using any sorting algo

# def swap(arr, l, mid):
#     arr[l], arr[mid] = arr[mid], arr[l]
#     return arr
#
#
# def array_sort(arr):
#     low = 0
#     mid = 0
#     high = len(arr) - 1
#     while mid < high:
#         if arr[mid] == 0:
#             swap(arr, low, mid)
#             low = low + 1
#             mid = mid + 1
#         elif arr[mid] == 1:
#             mid = mid + 1
#         else:
#             swap(arr, mid, high)
#             high = high - 1
#             mid = mid + 1
#     return arr
#
#
# print(array_sort([2, 0, 2, 1, 1, 0, 0]))

# Array	Move all the negative elements to one side of the array

# arr = [2, 5, 6, -1, -1, 8, 9, 5, 7, -1, 8]
#
# def move_negative_elements_to_one_side(array):
#   j = 0
#   for i in range(len(array)):
#     if array[i] < 0:
#       array[i], array[j] = array[j], array[i]
#       j += 1
#   return array
# print(move_negative_elements_to_one_side(arr))


# Array	Find the Union and Intersection of the two sorted arrays.


# def union_and_intersection(arr1, arr2):
#     result = arr1
#
#     for i in range(len(arr2)):
#         if arr2[i] not in arr1:
#             result.append(arr2[i])
#
#     print(result)
#
#
# print(union_and_intersection([3, 1, 5, 6, 7], [5, 6, 2, 3, 6]))

# Array	Write a program to cyclically rotate an array by one.

# def rotate(arr, n):
#     i = 0
#     j = n - 1
#     while i != j:
#         arr[i], arr[j] = arr[j], arr[i]
#         i = i + 1
#     pass
#
#
# # Driver function
# arr= [1, 2, 3, 4, 5]
# n = len(arr)
# print ("Given array is")
# for i in range(0, n):
#     print (arr[i], end = ' ')
#
# rotate(arr, n)
#
# print ("\nRotated array is")
# for i in range(0, n):
#     print (arr[i], end = ' ')


# Array	find Largest sum contiguous Subarray [V. IMP]


# Array	Minimise the maximum difference between heights [V.IMP]	

# Array	Minimum no. of Jumps to reach end of an array	
# 16
# Array	find duplicate in an array of N+1 Integers	
# 17
# Array	Merge 2 sorted arrays without using Extra space.	
# 18
# Array	Kadane's Algo [V.V.V.V.V IMP]	
# 19
# Array	Merge Intervals	
# 20
# Array	Next Permutation	
# 21
# Array	Count Inversion	
# 22
# Array	Best time to buy and Sell stock	
# 23
# Array	find all pairs on integer array whose sum is equal to given number	
# 24
# Array	find common elements In 3 sorted arrays	
# 25
# Array	Rearrange the array in alternating positive and negative items with O(1) extra space	
# 26
# Array	Find if there is any subarray with sum equal to 0	
# 27
# Array	Find factorial of a large number	
# 28
# Array	find maximum product subarray	
# 29
# Array	Find longest consecutive subsequence

# Array	Given an array of size n and a number k, find all elements that appear more than " n/k " times.
# 31
# Array	Maximum profit by buying and selling a share atmost twice	
# 32
# Array	Find whether an array is a subset of another array	
# 33
# Array	Find the triplet that sum to a given value	
# 34
# Array	Trapping Rain water problem	
# 35
# Array	Chocolate Distribution problem	

# Array	Smallest Subarray with sum greater than a given value	

# Array	Three way partitioning of an array around a given value
# 38
# Array	Minimum swaps required bring elements less equal K together	
# 39
# Array	Minimum no. of operations required to make an array palindrome	

# Array	Median of 2 sorted arrays of equal size	

# Array	Median of 2 sorted arrays of different size.


# permutation

# def perm1(lst):
#     if len(lst) == 0:
#         return []
#     elif len(lst) == 1:
#         return [lst]
#
#     else:
#         l = []
#         for i in range(len(lst)):
#             print(l)
#             x = lst[i]
#             xs = lst[:i] + lst[i + 1:]
#             for p in perm1(xs):
#                 l.append([x] + p)
#     return l
# print(perm1([1,2,3]))


# byte_array = bytearray('XYZ', 'utf-8')
# print('Before update:', byte_array)
#
# mem_view = memoryview(byte_array)
#
# mem_view[2] = 74
# print('After update:', byte_array)

def kadane_algo(arr):
    maximum_end = 0
    maximum_so_Far = 0
    for i in range(len(arr)):
        maximum_end = maximum_end + arr[i]
        if maximum_end > maximum_so_Far:
            maximum_so_Far = maximum_end
        if maximum_end < 0:
            maximum_end = 0
    return maximum_so_Far


print(kadane_algo([-2, -3, 4, -1, -2, 1, 5, -3]))
