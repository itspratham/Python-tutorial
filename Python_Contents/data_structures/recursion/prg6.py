import threading
import time
from functools import partial


# def recursion(n):
#     if n < 5:
#         return
#     print(n)
#     recursion(n - 1)
#     # print("hello", n)
#     recursion(n - 2)


# f = time.time()
# recursion(20)
# t = time.time()
# print(t-f)


# from concurrent.futures import ThreadPoolExecutor
# #
# # # create a thread pool with 2 threads
# with ThreadPoolExecutor() as executor:
#     f = time.time()
#     executor.map(recursion, [20])
#     t = time.time()
#     print(t-f)
# print("Main thread continuing to run")


# 0.00517582893371582 - 209.584426879882812e-05


# # A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8….
#
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# for i in range(20):
#     print(fib(i))


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return self.head
#         else:
#             cur_node = self.head
#             while cur_node.next:
#                 cur_node = cur_node.next
#             cur_node.next = new_node
#
#     def print_ll(self):
#         if self.head is None:
#             return "Empty"
#         while self.head:
#             print(self.head.data)
#             self.head = self.head.next
#         return
#
#
#
#
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(1)
# ll.append(3)
# ll.print_ll()

# class A:
#     f = "fjf"
#
#     def get(self):
#         return self.f
#
#     def sett(self, g):
#         self.f = g
#
#
# a = A()
# print(a.f)
# a.sett("55")
# print(a.f)
# A.f = "33"
# print(A.f)


# Ques1:
# Python script to get the sum of all the digits of a
# multi-digit number. Repeat until the final sum
# is a single digit number.


def prime_no(number):
    number1 = number
    summ = 0
    while number > 0:
        summ += number% 10
        number //= 10
    if number1 >= 2:
        for i in range(2, ((number1//2)+1)//2):
            if number1%i == 0:
                return summ, None
        else:
            return summ, True
    else:
        return summ, None

print(prime_no(38))
