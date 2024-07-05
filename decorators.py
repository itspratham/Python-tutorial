# from collections import defaultdict
#
# f = ['ate', 'tea', 'node', 'done', 'soup']
#
#
# def check_(item, item_to_be_checked):
#     dict1 = {}
#     dict2 = {}
#     for i in range(len(item)):
#         if item[i] not in dict1:
#             dict1[item[i]] = 1
#         else:
#             dict1[item[i]] = dict1[item[i]] + 1
#     for i in range(len(item_to_be_checked)):
#         if item_to_be_checked[i] not in dict2:
#             dict2[item_to_be_checked[i]] = 1
#         else:
#             dict2[item_to_be_checked[i]] = dict2[item_to_be_checked[i]] + 1
#     return dict1 == dict2
#
#
# def anagrams(data):
#     dictionary = defaultdict(list)
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[j] not in dictionary.values():
#                 if check_(data[i], data[j]):
#                     dictionary[data[i]].append(data[j])
#     else:
#         dictionary[data[i]] = []
#     a_list = []
#     for key, values in dictionary.items():
#         a_list1 = [key]
#         a_list1.extend(values)
#         a_list.append(a_list1)
#     return a_list
#
#
# print(anagrams(f))

class A(object):     # deriving from 'object' declares A as a 'new-style-class'
    def foo(self):
        print ("foo")

class B(A):
    def foo(self):
        super(B, self).foo()   # calls 'A.foo()'

myB = B()
myB.foo()