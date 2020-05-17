# 1. Write a Python program to sort (ascending and descending) a dictionary by value.

# import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print('Original dictionary : ',d)
# sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1)))
# print('Dictionary in ascending order by value : ',sorted_d)
# sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
# print('Dictionary in descending order by value : ',sorted_d)



# 2. Write a Python program to add a key to a dictionary.
#
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# d = {0: 10, 1: 20}
# d[2] = 30
# print(d)



# 3. Write a Python program to concatenate following dictionaries to create a new one.
#
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3): dic4.update(d)
# print(dic4)





# 4. Write a Python program to check whether a given key already exists in a dictionary.

# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_present(x):
#   if x in d:
#       print('Key is present in the dictionary')
#   else:
#       print('Key is not present in the dictionary')
# is_key_present(5)
# is_key_present(9)


# 5. Write a Python program to iterate over dictionaries using for loops.

# d = {'x': 10, 'y': 20, 'z': 30}
# for dict_key, dict_value in d.items():
#     print(dict_key,':',dict_value)



# 6. Write a Python program to generate and print a dictionary
# that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# def square(n):
#     d =dict()
#     for i in range(1,n+1):
#         d[i] = i * i
#     return d
#
# print(square(5))



# 7. Write a Python program to print a dictionary
# where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
# 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# def square(n):
#     d =dict()
#     for i in range(1,n+1):
#         d[i] = i * i
#     return d
#
# print(square(15))




# 8. Write a Python program to merge two Python dictionaries.

# d1 = {1:1,2:2}
# d2 = {3:3,4:4}
# d3 ={}
# for d in (d1,d2):
#     d3.update(d)
# print(d3)



# 9. Write a Python program to iterate over dictionaries using for loops.

# d = {'Red': 1, 'Green': 2, 'Blue': 3}
# for color_key, value in d.items():
#      print(color_key, 'corresponds to ', d[color_key])



# 10. Write a Python program to sum all the items in a dictionary.

# d = {0:1,1:2,2:3}
#
# print(sum(d.values()))


# 11. Write a Python program to multiply all the items in a dictionary.

# import math
# d = {0:1,1:2,2:3}
#
# print(math.prod(d.values()))

# prod =1
# for i in d.values():
#     prod = i * prod
#
# print(prod)




# 12. Write a Python program to remove a key from a dictionary.

# d = {0:1,1:2,3:4}
# d.pop(1)
#
# print(d)

# 13. Write a Python program to map two lists into a dictionary.

# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# color_dictionary = dict(zip(keys, values))
# print(color_dictionary)



# 14. Write a Python program to sort a dictionary by key.

# import operator
# d= {3:4,1:0,2:8,0:5}
# d = dict(sorted(d.items(),key=operator.itemgetter(min(d.keys()))))
# print(d)



# 15. Write a Python program to get the maximum and minimum value in a dictionary.
# d= {3:4,1:0,2:8,0:5}
# print("Max value:",max(d.values()))
# print("Min value:",min(d.values()))





# 16. Write a Python program to get a dictionary from an object's fields.

# class dictObj(object):
#     def __init__(self):
#         self.x = 'red'
#         self.y = 'Yellow'
#         self.z = 'Green'
#
#     def do_nothing(self):
#         pass
#
#
# test = dictObj()
# print(test.__dict__)


# 17. Write a Python program to remove duplicates from Dictionary.
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# }
#
# result = {}
#
# for key,value in student_data.items():
#     if value not in result.values():
#         result[key] = value
#
# print(result)



# 18. Write a Python program to check a dictionary is empty or not.

# d = {}
# def dictt(d):
#     return len(d) == 0
#
# print(dictt(d))



# 19. Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


# from collections import Counter
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d = Counter(d1) + Counter(d2)
# print(d)



# 20. Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
#      {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print("Original List: ",L)
# for dic in L:
#     for val in dic.values():
#         print(val,end=" ")
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)




# 21. Write a Python program to create and display
# all combinations of letters, selecting each letter from a different key in a dictionary. 
# program
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
# program


# import itertools
#
# d = {'1': ['a', 'b'], '2': ['c', 'd']}
# for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
#     print(''.join(combo))

# 22. Write a Python program to find the highest 3 values in a dictionary.
# from heapq import nlargest
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# three_largest = nlargest(3, my_dict, key=my_dict.get)
# print(three_largest)


# 23. Write a Python program to combine values in python list of dictionaries. program
# Sample data: [{'item': 'item1', 'amount': 400},
# {'item': 'item2', 'amount': 300},
# {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
# program


# from collections import Counter
# item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# result = Counter()
# for d in item_list:
#     result[d['item']] += d['amount']
# print(result)



# 24. Write a Python program to create a dictionary from a string. program
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
# program

# str1 = 'w3resource'
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)


# 25. Write a Python program to print a dictionary in table format. program
# program
# 
# 26. Write a Python program to count the values associated with key in a dictionary. program
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True
# program
# 
# 27. Write a Python program to convert a list into a nested dictionary of keys. program
# program


# 28. Write a Python program to sort a list alphabetically in a dictionary. program
# program




# 29. Write a Python program to remove spaces from dictionary keys. program
# program
# 
# 30. Write a Python program to get the top three items in a shop. program
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
# program
# 
# 31. Write a Python program to get the key, value and item in a dictionary. program
# program
# 
# 32. Write a Python program to print a dictionary line by line. program
# program
# 
# 33. Write a Python program to check multiple keys exists in a dictionary. program
# program
# 
# 34. Write a Python program to count number of items in a dictionary value that is a list. program
# program
# 
# 35. Write a Python program to sort Counter by value. program
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
# program
# 
# 36. Write a Python program to create a dictionary from two lists
# without losing duplicate values. program
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})
# program

# l1=['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# l2= [1, 2, 2, 3]
# d = dict(zip(l1,l2))
# print(d)


# 37. Write a Python program to replace dictionary values with their  average. program
# program

# def sum_math_v_vi_average(list_of_dicts):
#     for d in list_of_dicts:
#         n1 = d.pop('V')
#         n2 = d.pop('VI')
#         d['V+VI'] = (n1 + n2)/2
#     return list_of_dicts
# student_details= [
#   {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
#   {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
#   {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# ]
# print(sum_math_v_vi_average(student_details))


# 38. Write a Python program to match key values in two dictionaries. program
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
# program


# d1 ={'key1': 1, 'key2': 3, 'key3': 2}
# d2 = {'key1': 1, 'key2': 2}
# def two_dict(d1,d2):
#     for key,value in d1.items():
#         if key in d2.keys():
#             if value in d2.values():
#                 print(f"{key}: {value} is present in both d1 and d2")
#
# two_dict(d1,d2)


# 39. Write a Python program to store a given dictionary in a json file. program
# Original dictionary:
# {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
# <class 'dict'>
# Json file to dictionary:
# {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'},
# {'firstName': 'Mervin', 'lastName': 'Friedland'},
# {'firstName': 'Aron ', 'lastName': 'Wilkins'}],
# 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'},
# {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
# program






# 40. Write a Python program to create a dictionary of
# keys x, y, and z where each key has as value a list from 11-20, 21-30,
# and 31-40 respectively. Access the fifth value of each key from the dictionary. program
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]
# program

# d={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
#
# for key in d.keys():
#    print(d[key][4])


#perm.py
import time
def perm1(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        #import pdb; pdb.set_trace()
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            print(x,"x")
            print(xs, "xs")
            for p in perm1(xs):
                # print(p,"p")
                l.append([x] + p)
            print(l,"l")
        return l

print(perm1(["a","b","c"]))