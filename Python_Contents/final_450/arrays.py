# Reverse the array
# def reverse_arr(A, start, end):
#     while start < end:
#         A[start], A[end] = A[end], A[start]
#         start += 1
#         end -= 1
#     return A
#
#
# arr = [2, 4, 5, 8, 9, 1]
# print(reverse_arr(arr, 0, 5))


# def reverseList(A, start, end):
#     while start < end:
#         A[start], A[end] = A[end], A[start]
#         start += 1
#         end -= 1
#     return A
#
#
# print(reverseList([1, 2, 3, 4, 5, 6], 0, 5))


# Find the maximum and minimum element in an array

# def max_min(arr):
#     max = arr[0]
#     min = arr[0]
#     for i in range(len(arr)):
#         if arr[i] > max:
#             max = arr[i]
#         if arr[i] < min:
#             min = arr[i]
#     print("the max is: ", max)
#     print("the min is: ", min)
#
#
# max_min([4, 5, 6, 22, 556, 66])

# Find the "Kth" max and min element of an array
# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
# Move all the negative elements to one side of the array 
# Find the Union and Intersection of the two sorted arrays.
# Write a program to cyclically rotate an array by one.
# find Largest sum contiguous SubArray [V. IMP]
# Minimise the maximum difference between heights [V.IMP]
# Minimum no. of Jumps to reach end of an array
# find duplicate in an array of N+1 Integers
# Merge 2 sorted arrays without using Extra space.
# Kadane's Algo [V.V.V.V.V IMP]
# Merge Intervals
# Next Permutation
# Count Inversion
# Best time to buy and Sell stock
# find all pairs on integer array whose sum is equal to given number
# find common elements In 3 sorted arrays
# Rearrange the array in alternating positive and negative items with O(1) extra space
# Find if there is any SubArray with sum equal to 0
# Find factorial of a large number
# find maximum product SubArray 
# Find longest consecutive subsequence
# Given an array of size n and a number k, fin all elements that appear more than " n/k " times.
# Maximum profit by buying and selling a share utmost twice


# Find whether an array is a subset of another array
# Python3 program to find all subsets
# by backtracking.
# In the array A at every step we have two
# choices for each element either we can
# ignore the element or we can include the
# element in our subset


def subsetsUtil(A, subset, index):
    print(*subset)
    for i in range(index, len(A)):
        # include the A[i] in subset.
        subset.append(A[i])

        # move onto the next element.
        subsetsUtil(A, subset, i + 1)

        # exclude the A[i] from subset and
        # triggers backtracking.
        subset.pop(-1)
    return


# below function returns the subsets of vector A.
def subsets(A):
    subset = []

    # keeps track of current element in vector A
    index = 0
    subsetsUtil(A, subset, index)


# Driver Code

# find the subsets of below vector.
array = [1, 2, 3, 4]

# res will store all subsets.
# O(2 ^ (number of elements inside array))
# because at every step we have two choices
# either include or ignore.
# subsets(array)

# Find the triplet that sum to a given value
# Trapping Rain water problem
# Chocolate Distribution problem
# Smallest SubArray with sum greater than a given value
# Three way partitioning of an array around a given value
# Minimum swaps required bring elements less equal K together
# Minimum no. of operations required to make an array palindrome
# Median of 2 sorted arrays of equal size
# Median of 2 sorted arrays of different size
