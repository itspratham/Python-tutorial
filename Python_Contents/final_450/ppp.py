# Minimum number of jumps
# Given an array of N integers arr[] where each element represents
# the maximum length of the jump that can be made forward
# from that element. This means if arr[i] = x, then we can jump any
# distance y such that y ≤ x. Find the minimum number of jumps to reach the end
# of the array (starting from the first element). If an element is 0,
# then you cannot move through that element.
#
# Note: Return -1 if you can't reach the end of the array.
#
#
# Example 1:
#
# Input:
# N = 11
# arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
# Output: 3
# Explanation:
# First jump from 1st element to 2nd
# element with value 3. Now, from here
# we jump to 5th element with value 9,
# and from here we will jump to the last.
# Example 2:
#
# Input :
# N = 6
# arr = {1, 4, 3, 2, 6, 7}
# Output: 2
# Explanation:
# First we jump from the 1st to 2nd element
# and then jump to the last element.


# def jump_min(arr):
#     if len(arr) == 1:
#         return 0
#     elif len(arr) == 0:
#         return 0
#     else:
#         return 1 + jump_min(arr[arr[0]:])
#
#
# print(jump_min([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Given an array Arr[] of N integers.
# Find the contiguous subarray (containing at least one number)
# which has the maximum sum and return its sum.
#
#
# Example 1:
#
# Input:
# N = 5
# Arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# A Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which
# is a contiguous subarray.

# def array_contiguous(arr, k, j):
#     if j == len(arr):
#         return
#     for i in range(len(arr)):
#         print(arr[k:j])
#         array_contiguous(arr, k + 1, j + 1)
#
#
# array_contiguous([1, 2, 3, -2, 5], 0, 1)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Merge 2 sorted arrays without using Extra space.
