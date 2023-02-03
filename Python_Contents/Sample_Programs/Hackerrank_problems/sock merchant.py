# John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
# Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.
#
# For example, there are  socks with colors .
# There is one pair of color  and one of color .
# There are three odd socks left, one of each color.
# The number of pairs is .
#
# Function Description
#
# Complete the sockMerchant function in the editor below. It must return an integer representing the number of
# matching pairs of socks that are available.
#
# sockMerchant has the following parameter(s):
#
# n: the number of socks in the pile
# ar: the colors of each sock
# Input Format
#
# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers describing the colors  of the socks in the pile.
#
# Constraints
#
#  where
# Output Format
#
# Return the total number of matching pairs of socks that John can sell.
#
# Sample Input
#
# 9
# 10 20 20 10 10 30 50 10 20
# Sample Output
#
# 3


# Solution


# n = int(input())
# l = [int(x) for x in input().split()]
# q = [0 for x in range(101)]
#
# for i in l:
#     q[i] += 1
# print(q)
# ans = 0
# for i in q:
#     if i > 1:
#         ans += int(i / 2)
# print(ans)

# n = int(input())
# temp = input().split(' ')
# graph = {}
# for item in temp:
#     graph[item] = 0
# for item in temp:
#     graph[item] += 1
# count = 0
# for item in graph:
#     count += int(graph[item]/2)
# print(count)


# n = int(input())
# c = list(int(i) for i in input().split())
# cou = 0
# for i in set(c):
#     if (c.count(i) >= 2):
#         cou += c.count(i) // 2
# print(cou)

# n = int(input())
# c = list(int(i) for i in input().split())
# cout = 0
# for i in set(c):
#     if c.count(i) >= 2:
#         cout += c.count(i) // 2
# print(cout)
#
#
# def rotLeft(a, d):
#     for i in range(d):
#         f = a[0]
#         a.remove(f)
#         a.append(f)
#     return a
#
#
# print(rotLeft([5, 6, 8, 3, 4], 2))


# Python3 program to find the maximum depth of tree

# A binary tree node


class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node


# def maxDepth(node):
#     if node is None:
#         return 0
#
#     else:
#
#         # Compute the depth of each subtree
#         lDepth = maxDepth(node.left)
#         rDepth = maxDepth(node.right)
#
#         # # Use the larger one
#         # if lDepth > rDepth:
#         #     return lDepth + 1
#         # else:
#         #     return rDepth + 1
#         return 1+max(lDepth,rDepth)
#
#
# # Driver program to test above function
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# print("Height of tree is %d" % (maxDepth(root)))

# This code is contributed by Amit Srivastav


# Recursive Python program for insertion sort
# Recursive function to sort an array using insertion sort

def insertionSortRecursive(arr, n):
    # base case
    if n <= 1:
        return

    # Sort first n-1 elements
    insertionSortRecursive(arr, n - 1)
    '''Insert last element at its correct position
        in sorted array.'''
    last = arr[n - 1]
    j = n - 2

    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = last


# A utility function to print an array of size n
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


# Driver program to test insertion sort
arr = [12, 11, 13, 5, 6]
n = len(arr)
insertionSortRecursive(arr, n)
printArray(arr, n)

# Contributed by Harsh Valecha

