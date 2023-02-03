# # Python3 program to find the maximum depth of tree
#
# # A binary tree node
#
#
# class Node:
#
#     # Constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
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
#         return 1 + max(lDepth, rDepth)
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
#
# # This code is contributed by Amit Srivastav

#
# def a_func(n,count):
#     if n == 0:
#         return 1
#     print(n)
#     print("Process {}".format(count))
#     a_func(n - 1, count + 1)
#     a_func(n - 1, count + 1)
#
#
# a_func(3, 0)

#
# def fun(n):
#     if n >= 0:
#         fun(n - 1)
#         fun(n - 2)
#         fun(n - 4)
#         fun(n - 5)
#     print(n)
#     return


# fun(5)

# def func(n):
#     if n < 2:
#         return
#     func(n - 1)
#     func(n - 2)
#     func(n - 4)
#     print(n)
#
#
# func(5)


# def fun(n):
#     if n > 0:
#         fun(n - 1)
#         print(n, end=", ")
#         fun(n - 1)
#
# # driver code
#
#
# fun(5)
# # 4 3 2 1
# # 1 2 3 4
# # 1 2

# This code is contributed by shubhamsingh10


