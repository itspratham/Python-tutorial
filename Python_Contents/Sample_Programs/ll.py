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
#         headd = self.head
#         if self.head is None:
#             self.head = Node(data)
#             return
#         while headd.next is not None:
#             headd = headd.next
#         headd.next = Node(data)
#         return
#
#     def print_list(self):
#         headd = self.head
#         while headd:
#             print(headd.data)
#             headd = headd.next
#         return
#
#     def middle_element(self):
#         dict_map = dict()
#         headd = self.head
#         length = 0
#         while headd:
#             length = length + 1
#             dict_map[length] = headd.data
#             headd = headd.next
#         lee = length // 2
#         return dict_map[lee]
#
#     def find_the_third_element(self):
#         try:
#             a_list = []
#             headd = self.head
#             while headd:
#                 a_list.append(headd.data)
#                 headd = headd.next
#             return a_list[-2]
#         except:
#             return ""
#
#     def reverse_list(self):
#         prev = None
#         current = self.head
#         while current is not None:
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#         self.head = prev
#
#
# ll = LL()
# ll.append("A")
# ll.append("B")
# ll.append("C")
# ll.append("D")
# ll.append("E")
# ll.append("F")
# ll.append("G")
# ll.append("H")
# ll.print_list()
# # print(ll.middle_element())
# # print(ll.find_the_third_element())
# print("===============")
# ll.reverse_list()
# ll.print_list()

#
# def second_max(arr):
#     maxx = -999999
#     second_max = arr[0]
#     for i in range(len(arr)):
#         if arr[i] > maxx:
#             maxx = arr[i]
#     for j in range(len(arr)):
#         if arr[j] != maxx and arr[j] > second_max:
#             second_max = arr[j]
#     return second_max
#
#
# print(second_max([3, 4, 44, 56, 77, 78, 2]))


class MEthod_Overloading:

    def ssum(self, a, b, c=0):
        return a + b + c

    def ssum(self, a, b):
        return a + b


v = MEthod_Overloading()
print(v.ssum(a=4, b=5, c=7))
