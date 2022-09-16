# Given a string S. For each index i(1<=i<=N-1),
# erase it if s[i] is equal to s[i-1] in the string.

# Input:
# S = aabb
# Output:  ab
# Explanation: 'a' at 2nd position is
# appearing 2nd time consecutively.
# Similiar explanation for b at
# 4th position.

# class Solution:
#     def removeConsecutiveCharacter(self, S):
#         s=""
#         for i in range(len(S)-1):
#             if(S[i]!=S[i+1]):
#                 s+=S[i]
#         s+=S[-1]
#         return(s)
#         # code here
#
#
# #{
#  # Driver Code Starts
# #Initial Template for Python 3
#
# if __name__ == '__main__':
#     T = int(input())
#
#     for tcs in range(T):
#         s = input()
#         ob = Solution()
#         print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends

# 5 4 3 2 1
# 1 2

def a_func(target):

    if target > 0:
        a_func(target-1)
        print(target)
        a_func(target-1)
a_func(5)


# Write a program in C to print first 50 natural numbers using recursion.

# def func(n):
#     if n <= 5:
#         func(n + 1)
#         print(n)
#         func(n + 2)
#
#
# func(1)

# Write a program in C to reverse a string using recursion
# input = "w3resource"

# def recur(string, length):
#     if


# def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
#     if n == 0:
#         return
#     TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
#     print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
#     TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)
#
#
# # Driver code
# N = 3
#
# # A, C, B are the name of rods
# TowerOfHanoi(N, 'A', 'C', 'B')


# def recurse(n, s):
#     if n == 0:
#         print(s)
#     else:
#         recurse(n - 1, n + s)
#         recurse(n - 1, n + 2*s)
#
# recurse(2, 0)
