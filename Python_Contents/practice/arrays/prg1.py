# Array
# Check if pair with the given Sum exists in Array
# def check_Sum(arr, target, i, j):
#     if j == len(arr):
#         return
#     if arr[i] + arr[j] == target:
#         return f"{arr[i]} at {i + 1}", f"{arr[j]} at {j + 1}"
#     else:
#         return check_Sum(arr, target, i + 1, j + 1)
#
#
# print(check_Sum([1, 4, 5, 7, 2, 8], 12, 0, 1))

# Best Time to Buy and Sell Stock
# Find duplicates
# Product of Array Except Self
# Maximum Subarray
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.


# def maximum_Subarray(nums, j, maximum):
#     if j == len(nums) + 1:
#         return 0
#
#     for i in range(j, len(nums)):
#         maximum_Subarray(nums, j + 1, maximum)
#         print(nums[:i])
#         # if sum(nums[i:j]) > maximum:
#         #     maximum = sum(nums[i:j])
#     return maximum


# print(maximum_Subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4], 1, 0))
# Maximum Product Subarray
# Find Minimum in Rotated Sorted Array
# Search in Rotated Sorted Array
# 3 Sum
# Container With Most Water
# Find the Factorial of a large number
# Trapping Rain Water
# Chocolate Distribution Problem
# Insert Interval
# Merge Intervals
# Non-overlapping Intervals

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Matrix
# Set Matrix Zeroes
# a_matrix = [[1, 1, 1],
#             [1, 0, 1],
#             [1, 1, 1]]
#
# # Spiral Matrix
#
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 6],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]
#           ]
#
#
# def spiral_matrix(mat):
#     top = 0
#     left = 0
#     right = len(mat)-1
#     bottom = len(mat)-1
#     while top <= bottom and left <= right:
#         for i in range(left, right):
#             print(mat[top][i], end="->")
#
#         for i in range(top, bottom):
#             print(mat[i][right], end="->")
#
#         for i in range(right, left,-1):
#             print(mat[bottom][i], end="->")
#
#         for i in range(bottom, top,-1):
#             print(mat[i][left], end="->")
#         left += 1
#         bottom -= 1
#         right -= 1
#         top += 1
#
# spiral_matrix(matrix)
# Program to find the transpose of a matrix

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# def matrix_transpose(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print(matrix[j][i], end=" ")
#
# matrix_transpose(matrix)
# Word Search


# Python program showing
# abstract base class work
# Python program invoking a
# method using super()

# define Python user-defined exceptions
class Error(ArithmeticError):
	"""Base class for other exceptions"""
	pass

class zerodivision(Error):
	"""Raised when the input value is zero"""
	pass

try:
	i_num = int(input("Enter a number: "))
	if i_num == 0:
		raise zerodivision
except zerodivision:
	print("Input value is zero, try again!")
	print()
