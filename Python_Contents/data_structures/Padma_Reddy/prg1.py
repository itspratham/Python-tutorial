# #Through Euclid's algorithm
# def gcd(m, n):
#     while n != 0:
#         r = m % n
#         m = n
#         n = r
#
#     return m
#
#
# print(gcd(60, 200))


# Iterative approach
# def gcd(m,n):
#     if n==0:
#         return m
#     return gcd(n, m%n)
#
# x = gcd(60,200)
# print(x)


# def gcd(m,n):
#     while m !=n:
#         if m>n:
#             m = m-n
#         else:
#             n = n-m
#
#     return m

# print(gcd(60, 200))


# to compute gcd using consecutive integer checking
# def gcd(m,n):
#     small = min(m, n)
#     while 1:
#         if m % small == 0:
#            if n % small == 0:
#                 return small
#         small = small - 1
#
# print(gcd(60,200))


# Program for finding the largest number of an array
# l = [1,4,5,62,3,2,10,56]
# def largest(l):
#     big = l[0]
#     for i in range(1,len(l)-1):
#         if l[i] > big:
#             big = l[i]
#     return big
#
# print(largest(l))


# Linear Search

# l= [83,3,4,5,434,3123,23133,442213]
#
# def linear_search(l):
#     integer = int(input("Enter the number to be searched: "))
#     for i in range(0,len(l)-1):
#         if integer == l[i]:
#             print(f"Number found at {i}")
#     else:
#         print("Number not found")
#
#     return
#
# linear_search(l)


# Element uniqueness problem
# l = [4, 6, 7, 78, 3, 3, 2, 7, 6]
# l1 = [4, 6, 78, 3, 2, 7]
#
#
# def Element_uniqueness_problem(l):
#     for i in range(0, len(l) - 2):
#         for j in range(i + 1, len(l) - 1):
#             if l[i] == l[j]:
#                 print(f"{l[i]} is  present both at {i} and {j} position ")
#
#     return f"The list is distinct"


# print(Element_uniqueness_problem(l))
# Element_uniqueness_problem(l1)

# Factorial Problem
# def factorial(n):
#     if  n==0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# print(factorial(8))


# Multiplication of two matrices
# def Multiplication_of_two_matrices():


# Tower OF hanoi
# def towers(n, source, destination, spare):
#     #count = 0
#     if n == 1:
#         print('move From', source, ' to destination ', destination)
#         return 1
#     else:
#         #count += towers(n-1, source, spare, destination)
#         towers(n - 1, source, spare, destination)
#         #count += towers(1, source, destination, spare)
#         print('move From', source, ' to destination ', destination)
#         #count += towers(n-1, spare, destination, source)
#         towers(n - 1, spare, destination, source)
#         return
# print(towers(3, 'A', 'C', 'B'))


# Fibonacci Numbers
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(5))
