"""
Valid balanced parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Input: s = "()[]{}"
Output: true

Input: s = "([((({[[]]})))])[]{}"
Output: true

Input: s = "(){}["
Output: false

Input: s = "(]"
Output: false

Input: s = "()([])]]]"
Output: false

Input: s = "]()()"
Output: false
"""
from pydantic.tools import lru_cache

import functools


# class Stack:
#     def __init__(self):
#         self.a_list = []
#
#     def push(self, item):
#         self.a_list.append(item)
#
#     def pop(self):
#         return self.a_list.pop()
#
#     def is_empty(self):
#         return True if len(self.a_list) == 0 else False
#
#
# @lru_cache(100000)
# def is_valid_brackets(s):
#     a_list = Stack()
#     count = 0
#     while count < len(s):
#         print(a_list.a_list, "hello")
#         if s[count] in ('{', "(", "["):
#             a_list.push(s[count])
#         else:
#             if not a_list.is_empty():
#                 f = a_list.pop()
#                 if f == "{":
#                     print(s[count], f)
#                     if not s[count] == "}":
#                         return False
#                 if f == "[":
#                     print(s[count], f)
#                     if not s[count] == "]":
#                         return False
#                 if f == "(":
#                     print(s[count], f)
#                     if not s[count] == ")":
#                         return False
#             else:
#                 return False
#         count = count + 1
#     if a_list.a_list:
#         return False
#     return True
#
#
# print(is_valid_brackets("(){}[]"))



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
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
#     def print_the_ll(self):
#         while self.head is not None:
#             print(self.head.data)
#             self.head = self.head.next
# ll = LinkedList()
# ll.append("4")
# ll.append("5")
# ll.append("6")
# ll.print_the_ll()

def permutations(string):
    if len(string) == 0:
        return [""]

    permutations1 = []

    for character in string:
        for permutation in permutations(string[1:]):
            permutations1.append(character + permutation)

    return permutations1

permutations = permutations("abc")

for permutation in permutations:
    print(permutation)