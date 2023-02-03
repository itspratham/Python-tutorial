# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# class Tree:
#     def __init__(self):
#         pass
#
#     def pre_order(self, root, traversal):
#         if root:
#             traversal = self.pre_order(root.left, traversal)
#             traversal += str(root.data) + "->"
#             print(traversal)
#             traversal = self.pre_order(root.right, traversal)
#         return traversal
#
#
# obj = Tree()
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
# print(obj.pre_order(root, ""))


from sys import setrecursionlimit


# def add_the_Number(n):
#     str_n = str(n)
#     result = 0
#     for i in range(len(str_n)):
#         result = result + (int(str_n[i]) * int(str_n[i]))
#     return result
#
#
# def isHappy(n):
#     if len(str(n)) == 1 and n != 1:
#         print(False)
#         return False
#     elif n == 1:
#         print(True)
#         return True
#     else:
#         number = add_the_Number(n)
#         isHappy(number)
#
#
#
# isHappy(101)


# def binary_search(arr, target):
#     if len(arr) == 0:
#         raise "Empty array provided"
#     low = 0
#     high = len(arr) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return "It's not Found"
#
#
# print(binary_search([2], 4))


# class B:
#     def method1(self):
#         pass
#
#     def __method2(self):
#         print("hello")
#
# class A(B):
#
#     def method3(self):
#         self.__method2()
#
#
# obj = A()
# obj.method3()


# def fib(n, f=None):
#     if f is None:
#         f = {}
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     if n in f:
#         print(f)
#         return f[n]
#     else:
#         f1 = fib(n - 1) + fib(n - 2)
#         f[n] = f1
#     return f1
#
#
# fib(7)


# def fastFib(n, memo):
#     global numCalls
#     numCalls += 1
#     # print('fib1 called with', n)
#     print(memo)
#     if n not in memo:
#         memo[n] = fastFib(n - 1, memo) + fastFib(n - 2, memo)
#     return memo[n]
#
#
# def fib1(n):
#     memo = {0: 1, 1: 1}
#     return fastFib(n, memo)

#
# numCalls = 0
# n = 6
# res = fib1(n)
# print('fib of', n, '=', res, 'numCalls = ', numCalls)
