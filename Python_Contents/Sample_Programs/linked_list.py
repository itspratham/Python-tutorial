class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        cur_node = self.head
        new_node = Node(data)
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next =new_node


    def print_list(self):
        currnode = self.head
        while currnode:
            print(currnode.data)
            currnode = currnode.next

    def delete_node(self,key):
        if self.head is None:
            print("No scope to delete the node")
            return
        curr_node = self.head
        if curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        prev = None
        while curr_node.data and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next

        prev.next = curr_node.next
        curr_node = None

    def insert_at_an_index(self,position,data):
        newnode = Node(data)
        if self.head is None:
            print("List is empty and I can insert for you at 1st position")
            self.append(data)
            return
        curr_node = self.head
        if self.head.next is None and position == 1:
            self.head = newnode
            newnode.next = curr_node
            return
        prev = None
        count = 1

        while count!=position:
            prev = curr_node
            curr_node = curr_node.next
            count = count+1
        prev.next = newnode
        newnode.next = curr_node

    def rotate_left(self,position):
        if self.head is None and position<=0:
            return
        if self.head and position==1:
            return

        headd = self.head
        curr_node = self.head
        prev = None
        count = 0
        while curr_node and count<position:
            prev = curr_node
            headd = headd.next
            curr_node = curr_node.next
            count = count + 1
        curr_node = prev

        while headd:
            prev =headd
            headd = headd.next

        headd = prev
        headd.next = self.head
        self.head = curr_node.next
        curr_node.next = None





l = LinkedList()
l.append("A")
l.append("B")
l.append("C")
l.append("D")
l.append("E")
l.rotate_left(3)
l.print_list()


# # !/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# def func(arr, k):
#     l = []
#     for i in range(len(arr)):
#         l.append(arr[i][k])
#     l = l.sort()
#     print(l)
#     for i in range(len(arr)):
#         arr[i].insert(k, l[i])
#
#     for i in range(len(arr)):
#         print(arr[i])
#
#
# if __name__ == '__main__':
#     nm = input().split()
#
#     n = int(nm[0])
#
#     m = int(nm[1])
#
#     arr = []
#
#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))
#
#     k = int(input())
#     func(arr, k)
