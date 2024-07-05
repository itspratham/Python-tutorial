# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Tree
# Maximum Depth of Binary Tree

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# class Tree:
#     def printPreorder(self, root):
#         if root is None:
#             return
#         print(root.data, end=" ")
#         self.printPreorder(root.left)
#         self.printPreorder(root.right)
#
#     def height_of_the_tree(self, root):
#         if root is None:
#             return 0
#         else:
#             return max(self.height_of_the_tree(root.left),
#                        self.height_of_the_tree(root.right))+1
#
#
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.right = Node(6)
# root.right.right.left = Node(7)
# f = Tree()
# f.printPreorder(root)
# print(f.height_of_the_tree(root))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Check if two trees have the same structure
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# class Tree:
#     def checks(self, node1, node2):
#         if node1 is None and node2 is None:
#             return True
#         if node1 is not None and node2 is not None:
#             return (node1.data == node2.data and self.checks(node1.left, node2.left)
#                     and self.checks(node1.right, node2.right))
#         return False
#
#
# root1 = Node(1)
# root2 = Node(1)
# root1.left = Node(2)
# root1.right = Node(3)
# root1.left.left = Node(4)
# root1.left.right = Node(5)
#
# root2.left = Node(2)
# root2.right = Node(3)
# root2.left.left = Node(4)
# root2.left.right = Node(5)
# root2.left.left.right = Node(9)
#
# t = Tree()
# print(t.checks(root1, root2))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Invert/Flip Binary Tree
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class Tree:
#     def PrintTree(self, root):
#         if root.left:
#             self.PrintTree(root.left)
#         print(root.data, end=' '),
#         if root.right:
#             self.PrintTree(root.right)
#     def flip(self, root):
#         if root is None:
#             return None
#         root.left, root.right = self.flip(root.right), self.flip(root.left)
#         return root
#
# tree = Node(10)
# tree.left = Node(20)
# tree.right = Node(30)
# tree.left.left = Node(40)
# tree.right.right = Node(50)
# print('Initial Tree :',end = ' ' )
# g = Tree()
# g.PrintTree(tree)
# g.flip(root=tree)
# print('\nInverted Tree :', end=' ')
# g.PrintTree(tree)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Maximum Path Sum

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Binary Tree Level Order Traversal
# Serialize and Deserialize Binary Tree
# Subtree of Another Tree
# Construct Binary Tree from Preorder and Inorder Traversal
# Validate Binary Search Tree
# Kth Smallest Element in a BST
# Lowest Common Ancestor of BST
# Implement Trie (Prefix Tree)
# Add and Search Word
