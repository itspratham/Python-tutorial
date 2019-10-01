# #Insertion Sort
#
# t = int(input("enter the test"))
# def main(t):
#     # Write code here
#     for i in range(t):
#         n = int(input("enter the number"))
#         if n == 0:
#             print("0")
#         elif n == 1:
#             print("1")
#         else:
#             listt = [1, 1]
#             h = 1
#             #import pdb; pdb.set_trace()
#             for j in range(n):
#                 if len(listt)>=n:
#                     break
#                 pattern = listt[2*j+1] + listt[2*j]
#                 listt.append(pattern)
#                 if len(listt)>=n:
#                     break
#                 pattern1 = pattern // listt[2*j+1]
#                 listt.append(pattern1)
#                 if len(listt)>=n:
#                     break
#             str1 = ' '.join(str(e) for e in listt)
#             print(str1+' ')
#
# main(t)




















# Cadbury Problem (100 Marks)
# In DPS School, Cadbury bars have to be distributed to children waiting in a queue. Each Cadbury bar is rectangular in shape and its side lengths are integer values.
#
# The distribution procedure is as follows:-
#
# 1. If bar is not square in shape, then the largest possible square piece of Cadbury is broken and given to the first child in queue.
# 2. If bar is square in shape, then complete bar is given to the first child in queue.
#
# Once a child receives his share of Cadbury, he leaves the queue. The remaining portion of the Cadbury bar is dealt in same fashion and the whole or a portion of it is given to the next child in the queue.
#
# School has got a carton of Cadbury bars to be distributed among the children all over the School. The Cadbury bars in the carton are of different sizes. A bar of length i and breadth j is considered to be different from a bar of length j and breadth i.
#
# For every i such that M<=i<=N and every j such that P<=j<=Q (where M, N, P and Q are integers). Each Cadbury bar in carton is unique in length (i) and breath(j).
#
# Given the values of M, N, P and Q (where M, N values are the ranges for length of Cadbury and P, Q values are the ranges for breadth of Cadbury). Find the number of children who will receive Cadbury from the carton.
#
#
# Input Format
# Your program need to read 4 integers M, N, P, Q from STDIN.
# (M, N values are the ranges for length of Cadbury bar. P, Q values are the ranges for breadth of Cadbury bar).
#
#
# Constraints
# 1 <= M, N, P and Q <= 200
#
# Output Format
# You need to print the number of children who will receive Cadbury bar from the carton.
#
# Sample TestCase 1
# Input
# 5
# 6
# 3
# 4
# Output
# 14
# Explanation
# M = 5, N = 6, P = 3, Q=4
#
# Here, i can be from 5 to 6 and j can be from 3 to 4. So the four bars will be in carton of sizes 5x3, 5x4, 6x3, 6x4.
#
# First we choose a cadbury bar of size 5x3
# first child would receive 3x3 portion ( remaining 2x3 portion )
# next child would receive 2x2 portion ( remaining 2x1 portion )
# now the remaining portion are 2 square pieces of (1x1), which can be given to 2 more children
#
# So the Cadbury bar with the size of 5x3 can be distributed to 4 children.
#
# Similarly we can find out number of children for rest of the combinations (i.e. 5x4, 6x3, 6x4) in the given range as follows
#
#
#
# Cadbury bar with the size of 5x3 can be distributed to 4 children.
# Cadbury bar with the size of 5x4 can be distributed to 5 children.
# Cadbury bar with the size of 6x3 can be distributed to 2 children.
# Cadbury bar with the size of 6x4 can be distributed to 3 children.
#
# So the whole carton can be distributed among 14 children. Hence the output will be 14.







test_case= int(input("enter thr test "))

for i in range(test_case):
    money= int(input(" money "))
    no_of_flavours = int(input("flavour "))
    cost= input("cosy ").split()
    cost= list(map(int,cost))
    for j in range(len(cost)-1):
        if (cost[j]+cost[j+1])==money:
            a=cost.index(cost[j])
            b= cost.index(cost[j+1])
            print(a,b)