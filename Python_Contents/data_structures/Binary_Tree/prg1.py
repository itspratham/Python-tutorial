# How is a binary search tree implemented?

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# class BinaryTree:
#     def __init__(self, root):
#         self.root = Node(root)
#
#     def pre_order(self, start, traversal):
#         if start:
#             traversal += str(start.value) + "-"
#             traversal = self.pre_order(start.left, traversal)
#             traversal = self.pre_order(start.right, traversal)
#         return traversal
#
#
# bt = BinaryTree(1)
# bt.root.left = Node(2)
# bt.root.right = Node(3)
# bt.root.left.left = Node(4)
# bt.root.left.right = Node(5)
# bt.root.right.left = Node(6)
# bt.root.right.right = Node(7)
#
# print(bt.pre_order(bt.root, ""))

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# class BT:
#     def __init__(self, root):
#         self.root = Node(root)
#
#     def preorder(self, start, traversal):
#         if start:
#             traversal += str(start.value) + "-->"
#             traversal = self.preorder(start.left, traversal)
#             traversal = self.preorder(start.right, traversal)
#         return traversal
#
#
# bt = BT(1)
# bt.root.left = Node(2)
# bt.root.right = Node(3)
# bt.root.left.left = Node(4)
# bt.root.left.right = Node(5)
# bt.root.right.left = Node(6)
# bt.root.right.right = Node(7)
#
# print(bt.preorder(bt.root, ""))


# from functools import lru_cache
# from sys import setrecursionlimit
# setrecursionlimit(10**6)
#
#
# class GraduationCeremony:
#     def __init__(self, n, m):
#         # n: number of academic days
#         # m: cannot miss m or more classes consecutevly
#         if n < m or n < 0 or m < 0:
#             raise Exception("Invalid Inputs")
#
#         self.n = n
#         self.m = m
#
#     def solve1(self):
#
#         @lru_cache(None)
#         def rec(n, m):
#             if self.m == m:
#                 return 0
#             if n == 0:
#                 return 1
#
#             return rec(n - 1, 0) + rec(n - 1, m + 1)
#
#         x1 = rec(self.n, 0)  # total number of valid way to attend classes
#         x2 = rec(self.n - 1, 1)  # total number of way to miss last day
#
#         return f"{x2}/{x1}"
#
#
#
#     def run(self):
#         print('=' * 40)
#         print('n:', self.n, ', m:', self.m, '\n')
#         print('Solution 1:', self.solve1())
#         print()
#
#
# if __name__ == "__main__":
#     inputs = [(5, 4), (10, 4)]
#     for n, m in inputs:
#         obj = GraduationCeremony(n, m)
#         obj.run()


# Emp table - columns - Emp_Id , Full_Name, Joining_Date
# Salary Table - Emp_Id , Project , Salary
# Write a sql query to fetch employee names having a salary
# greater than or equal to $40000 and less than or equal to $60000

#
# select e.fullName from Emp e, Salary s inner join
# on e.Emp_Id = s.Emp_Id where s.salary between 40000 and 60000;
#
#
# select s.project, count(emp_id) as c from Salary s
# group by s.project order by c desc;
#


# write a sql query to fetch project-wise count of  employees
# sorted by the project's count in descending order

# P1 2
# P2 2
# P4 1


# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# print(fib(5))


# def fib(n):


# num = 10
# n1, n2 = 0, 1
# # print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
# print(n3, end=" ")
#
# print()
