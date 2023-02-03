arr = [1, 2, 3, 4, 5, 6]
# f = map(lambda x: x % 2 == 0, arr)


# f = [arr[i] for i in range(len(arr)) if arr[i] % 2 == 0]
# print(f)

# Write a program to return the biggest word present in a list containing names of month
f = ["March", "May", "April", "December"]

# def func(f):
#     global word
#     max = 0
#     dict = {}
#     for i in range(len(f)):
#         if len(f[i]) > max:
#             max = len(f[i])
#             word = f[i]
#     return word
#
#
# print(func(f))


# Python3 code to demonstrate working of
# Most frequent word in Strings List
# Using loop + max() + split() + defaultdict()
from collections import defaultdict

# initializing Matrix
test_list = ["gfg is best for geeks", "geeks love gfg", "gfg is best"]

# printing original list
print("The original list is : " + str(test_list))

temp = defaultdict(int)

# memoizing count
for sub in test_list:
    for wrd in sub.split():
        temp[wrd] += 1

# getting max frequency
res = max(temp, key=temp.get)

# printing result
print("Word with maximum frequency : " + str(res))
