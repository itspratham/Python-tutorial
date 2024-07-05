# Array


# Check if a pair with the given Sum exists in Array
# Input: arr[] = {0, -1, 2, -3, 1}, x= -2
# Output: Yes
# Explanation:  If we calculate the sum of the output, 1 + (-3) = -2

# def func(arr, target):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 return arr[i], arr[j]
#
#
# print(func(arr=[0, -1, 2, -3, 1], target=-2))


# Best Time to Buy and Sell Stock
# Find duplicates
# Product of Array Except Self
# Maximum Subarray
# Maximum Product Subarray
# Find Minimum in Rotated Sorted Array
# Search in Rotated Sorted Array
# 3-Sum
# Container With Most Water
# Find the Factorial of a large number

# def factorial(number):
#     if number == 0:
#         return 1
#     elif number == 1:
#         return 1
#     else:
#         return number *factorial(number-1)
# print(factorial(7))

# Trapping Rain Water
# Chocolate Distribution Problem
# Insert Interval
# Merge Intervals
# Non-overlapping Intervals

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Matrix
# Set Matrix Zeroes
# Spiral Matrix
# Program to find the transpose of a matrix
# Word Search

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# String
# Longest Substring Without Repeating Characters
# Longest Repeating Character Replacement
# Smallest window in a String containing all characters of other String
# Check whether two Strings are anagram of each other
# print all anagrams together
# Check if given Parentheses expression is balanced or not
# pattern1 = "({}[])"
# pattern2 = "[[[{}{]]]"
#
#
# class Stack:
#     def __init__(self):
#         self.a_list = []
#         return
#
#     def append(self, data):
#         self.a_list = [data] + self.a_list
#         return
#
#     def pop(self):
#         if len(self.a_list) == 0:
#             raise Exception
#         fff = self.a_list[0]
#         del self.a_list[0]
#         return fff
#
#
# def balancing_expression(string):
#     stack = Stack()
#     for i in range(len(string)):
#         if string[i] in "{[(":
#             stack.a_list.append(string[i])
#         else:
#             sttt = stack.a_list.pop()
#             if string[i] == "}":
#                 if not sttt == "{":
#                     return False
#             elif string[i] == ")":
#                 if not sttt == "(":
#                     return False
#             elif string[i] == "]":
#                 if not sttt == "[":
#                     return False
#             else:
#                 return False
#     return True
#
# k = balancing_expression(pattern2)
# print(k)
# Sentence Palindrome
# Longest Palindromic Substring


# Palindromic Substrings

# def perm_substrings(arr, i):
#     if i == len(arr):
#         print(arr)
#     for j in range(i, len(arr)):
#         arr[i], arr[j] = arr[j], arr[i]
#         perm_substrings(arr, i + 1)
#         arr[i], arr[j] = arr[j], arr[i]
#
#
# perm_substrings([2, 3, 4], 0)
# Longest Common Prefix

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Linked List
# Reverse a Linked List
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LL:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         if self.head is None:
#             self.head = Node(data)
#             return
#         headd = self.head
#         while headd.next is not None:
#             headd = headd.next
#         headd.next = Node(data)
#         return
#
#     def print_LL(self):
#         if self.head is None:
#             return
#         else:
#             while self.head is not None:
#                 print(self.head.data)
#                 self.head = self.head.next
#         return
#
#     def reverse(self):
#         previous = None
#         current = self.head
#
#         while current is not None:
#             next = current.next
#             current.next = previous
#             previous = current
#             current = next
#         self.head = previous
#         return self.head
#
#     def delete_nth_node(self, target_count):
#         count = 1
#         cur_node = self.head
#         while cur_node:
#             prev = cur_node
#             if count == 1:
#                 daata = cur_node.next
#                 cur_node.next = None
#                 self.head = daata
#                 return
#             cur_node = cur_node.next
#             count = count + 1
#             if count == target_count:
#                 daata = cur_node.next
#                 if daata is None:
#                     prev.next = None
#                     return
#                 cur_node.next = None
#                 prev.next = daata
#                 return self.head
#         return
#
#
# ll = LL()
# ll.append("A")
# ll.append("B")
# ll.append("C")
# # ll.print_LL()
# # ll.reverse()
# # ll.print_LL()
# ll.delete_nth_node(1)
# ll.append("D")
# ll.print_LL()

# Detect Cycle in a Linked List
# Merge Two Sorted Lists
# Merge K Sorted Lists
# Remove Nth Node From End Of List (Done)
# Reorder List
# Add 1 to a number represented as linked list
# Find the middle of a given linked list
# Delete last occurrence of an item from linked list

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Stack & Queue
# Convert Infix expression to Postfix expression
# class Stack:
#     def __init__(self):
#         self.list = []
#
#     def insert(self, data):
#         return self.list.insert(0, data)
#
#     def pop(self):
#         try:
#             f = self.list[0]
#             del self.list[0]
#             return f
#         except:
#             raise Exception
#
#     @property
#     def length_of(self):
#         return len(self.list)
#
#     def top_of_the_element(self):
#         if len(self.list) > 0:
#             return self.list[0]
#         else:
#             return -1
#
#
# def infix_to_postfix(expression):
#     expression_string = ""
#     priority_dict = {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1}
#     f = Stack()
#     count = 0
#     while count < len(expression):
#         if expression[count] not in ["*", '/', "+", "-", "^"]:
#             expression_string = expression_string + expression[count]
#         elif f.length_of == 0 and expression[count] in ["*", '/', "+", "-", "^"]:
#             f.insert(expression[count])
#         elif expression[count] in ["*", '/', "+", "-", "^"]:
#             if priority_dict[expression[count]] > priority_dict[f.top_of_the_element()]:
#                 f.insert(expression[count])
#             else:
#                 while (expression[count] in ["*", '/', "+", "-", "^"] and
#                        priority_dict[expression[count]] < priority_dict[f.top_of_the_element()]):
#                     popped_Data = f.pop()
#                     expression_string = expression_string + popped_Data
#                 else:
#                     expression_string = expression_string + expression[count]
#         count = count + 1
#     while f.length_of != 0:
#         popped_Data = f.pop()
#         expression_string = expression_string + popped_Data
#     return expression_string
#
#
# print(infix_to_postfix("A*B+C*D"))

# Next Greater Element
# Delete middle element of a stack
# Check mirror in n-ary tree
# The Celebrity Problem
# Length of the longest valid substring
# Print Right View of a Binary Tree
# Find the first circular tour that visits all petrol pumps

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Tree
# Maximum Depth of Binary Tree
# Check if two trees have the same structure
# Invert/Flip Binary Tree
# Binary Tree Maximum Path Sum
# Binary Tree Level Order Traversal
# Serialize and Deserialize Binary Tree
# Subtree of Another Tree
# Construct Binary Tree from Preorder and Inorder Traversal
# Validate Binary Search Tree
# Kth Smallest Element in a BST
# Lowest Common Ancestor of BST
# Implement Trie (Prefix Tree)
# Add and Search Word

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Heap
# Top K Frequent Elements
# Find Median from Data Stream
# Largest triplet product in a stream
# Connect n ropes with minimum cost

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Graph
# Clone Graph
# Course Schedule
# Pacific Atlantic Water Flow
# Number of Islands
# Longest Consecutive Sequence
# Snake and Ladder Problem
# Detect Cycle in a Directed Graph
# Bridges in a graph
# Check whether a given graph is Bipartite or not
# Find size of the largest region in Boolean Matrix
# Flood fill Algorithm
# Strongly Connected Components
# Topological Sorting

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Dynamic Programming
# Count ways to reach the n’th stair
# Coin Change
# 0/1 Knapsack Problem
# Longest Increasing Subsequence
# arr = [3, 10, 2, 1, 20, 30, 100]

# def lic(arr, i, j):
#     if len(arr) == i:
#         return -1
#     if len(arr) == j:
#         return -1
#     if arr[j] > arr[i]:
#         return 1 + lic(arr, i + 1, j)
#     else:
#         return lic(arr, i, j + 1)
#
#
# print(lic(arr, 0, 0))


# Longest Common Subsequence
# X = "GEEKSFORGEEKS"
# Y = "GEEKSFEEKS"
#
#
# def longest_common_subsequence(string1, string2, i, j, k, lis):
#     if i == len(string1):
#         return ""
#     if j == len(string2):
#         return ""
#     if string1[i] == string2[j]:
#         return longest_common_subsequence(string1, string2, i + 1, j + 1, k, []) + string1[i]
#     else:
#         return max(longest_common_subsequence(string1, string2, i + 1, j, k, lis),
#                    longest_common_subsequence(string1, string2, i, j + 1, k, lis))
#
#
# print(''.join(list(reversed(longest_common_subsequence(X, Y, 0, 0, "", [])))))

# Word Break Problem
# Dice Throw
# Egg Dropping Puzzle
# Matrix Chain Multiplication
# Combination Sum
# Subset Sum Problem

# Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output: True
# Explanation: There is a subset (4, 5) with sum 9.

#
# def subset_prob(arr, i, summ):
#     if i == len(arr):
#         return False
#     for j in arr[i-1:]:
#         print(j , arr[i])
#         if j + arr[i] == summ:
#             return True
#         else:
#             subset_prob(arr,i + 1, summ)
#     # return False
# x = [3, 34, 4, 12, 5, 2]
# print(subset_prob(x,1,9))


# Find maximum possible stolen value from houses
# Count Possible Decodings of a given Digit Sequence
# Unique paths in a Grid with Obstacles
# Jump Game
# Cutting a Rod
# Maximum Product Cutting

# The main function that returns maximum
# product obtainable from a rope of length n

# def maxProd(n):
#     # Base cases
#     if n == 0 or n == 1:
#         return 0
#
#     # Make a cut at different places
#     # and take the maximum of all
#     max_val = 0
#     for i in range(1, n - 1):
#         print(max_val, i * (n - i))
#         max_val = max(max_val, max(i * (n - i), maxProd(n - i) * i))
#
#     # Return the maximum of all values
#     return max_val
#
#
# # Driver program to test above functions
# print("Maximum Product is ", maxProd(10))

# This code is contributed
# by Sumit Sudhakar

# Count number of ways to cover a distance
