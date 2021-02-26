# John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
# Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.
#
# For example, there are  socks with colors .
# There is one pair of color  and one of color .
# There are three odd socks left, one of each color.
# The number of pairs is .
#
# Function Description
#
# Complete the sockMerchant function in the editor below. It must return an integer representing the number of
# matching pairs of socks that are available.
#
# sockMerchant has the following parameter(s):
#
# n: the number of socks in the pile
# ar: the colors of each sock
# Input Format
#
# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers describing the colors  of the socks in the pile.
#
# Constraints
#
#  where
# Output Format
#
# Return the total number of matching pairs of socks that John can sell.
#
# Sample Input
#
# 9
# 10 20 20 10 10 30 50 10 20
# Sample Output
#
# 3


# Solution


# n = int(input())
# l = [int(x) for x in input().split()]
# q = [0 for x in range(101)]
#
# for i in l:
#     q[i] += 1
# print(q)
# ans = 0
# for i in q:
#     if i > 1:
#         ans += int(i / 2)
# print(ans)

# n = int(input())
# temp = input().split(' ')
# graph = {}
# for item in temp:
#     graph[item] = 0
# for item in temp:
#     graph[item] += 1
# count = 0
# for item in graph:
#     count += int(graph[item]/2)
# print(count)


# n = int(input())
# c = list(int(i) for i in input().split())
# cou = 0
# for i in set(c):
#     if (c.count(i) >= 2):
#         cou += c.count(i) // 2
# print(cou)

n = int(input())
c = list(int(i) for i in input().split())
cout = 0
for i in set(c):
    if c.count(i) >= 2:
        cout += c.count(i) // 2
print(cout)


def rotLeft(a, d):
    for i in range(d):
        f = a[0]
        a.remove(f)
        a.append(f)
    return a


print(rotLeft([5, 6, 8, 3, 4], 2))
