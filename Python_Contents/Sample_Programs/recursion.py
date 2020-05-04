#Write a Python program to calculate the sum of a list of numbers.

# def list_sum(num_List):
#     import ipdbipdb.set_trace()
#     if len(num_List) == 1:
#         return num_List[0]
#     else:
#         return num_List[0] + list_sum(num_List[1:])
#
#
# print(list_sum([2, 4, 5, 6, 7]))



#Write a Python program of recursion list sum
# def recursive_list_sum(data_list):
# 	total = 0
# 	for element in data_list:
# 		if type(element) == type([]):
# 			total = total + recursive_list_sum(element)
# 		else:
# 			total = total + element
#
# 	return total
# print( recursive_list_sum([1, 2, [3,4],[5,6]]))


# Write a Python program to get the factorial of a non-negative integer.
#
# n=5
# def factorial(n):
#     if n ==0:
#         return 1
#     elif n ==1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# print(factorial(n))

#Write a Python program to solve the Fibonacci sequence using recursion.

# def Fibonacci_Series(n):
#     if n ==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return Fibonacci_Series(n-1)+Fibonacci_Series(n-2)
#
# print(Fibonacci_Series(7))

#Write a Python program to get the sum of a non-negative integer.

# def sumDigits(n):
#   if n == 0:
#     return 0
#   else:
#     return n % 10 + sumDigits(int(n / 10))
#
# print(sumDigits(345))
# print(sumDigits(45))



#Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0)

# def sum_series(n):
#   if n < 1:
#     return 0
#   else:
#     return n + sum_series(n - 2)
#
# print(sum_series(6))
# print(sum_series(10))




#Write a Python program to calculate the geometric sum of n-1.
# def geometric_sum(n):
#     if n < 0:
#         return 0
#     else:
#         return 1 / (pow(2, n)) + geometric_sum(n - 1)
#
#
# print(geometric_sum(7))
# print(geometric_sum(4))

#Write a Python program to calculate the value of 'a' to the power 'b'.
# def power(a,b):
#     if b<=0:
#         return 1
#     return a * power(a,b-1)
# print(power(23,4))

#Write a Python program to find  the greatest common divisor (gcd) of two integers.




#Sum of the series 1^1 + 2^2 + 3^3 + ….. + n^n using recursion
#Input: n = 2
# Output: 5
# 11 + 22 = 1 + 4 = 5
#
#
#
# Input: n = 3
# Output: 32
# 11 + 22 + 33 = 1 + 4 + 27 = 32

#
# Solving f(n)= (1) + (2*3) + (4*5*6) ... n using Recursion

# def seriesSum(calculated, current, N):
#     i = calculated
#     cur = 1
#     # checking termination condition
#     if (current == N + 1):
#         return 0
#
#     # product of terms till current
#     while (i < calculated + current):
#         cur *= i
#         i += 1
#     return cur + seriesSum(i, current + 1, N)
#
# N = 5
#
# print(seriesSum(1, 1, N))


# Program to Calculate e^x by Recursion

def epowerx(n):
    if n<1:
        return 1
    return 2.718 * epowerx(n-1)

print(epowerx(5))

p = 1.0
f = 1.0


def e(x, n):
    global p, f

    # Termination condition
    if (n == 0):
        return 1

    # Recursive call
    r = e(x, n - 1)

    # Update the power of x
    p = p * x

    # Factorial
    f = f * n

    return (r + p / f)


# Driver code

x = 5
n = 15
print(e(x, n))

# Sum of digit of a number using recursion


# Sum of even elements of an Array using Recursion


# Sum of natural numbers using recursion

def natural(i,n):
    if i<n:
        return 
    return i + natural(i+1)


# Sort the Queue using Recursion


# Product of 2 Numbers using Recursion


# Reversing a queue using recursion


# Product of 2 numbers using recursion | Set 2


# Generating all possible Subsequences using Recursion


# Generating subarrays using recursion


# Traverse a given Matrix using Recursion

#1 + 2 + …. (n-2) + (n-1) + n, which is n(n+1)/2.


#Following is the relation between num and len.
#  num = 2^len-1
# s[0] is 1 time printed
# s[1] is 2 times printed
# s[2] is 4 times printed
# s[i] is printed 2^i times
# s[strlen(s)-1] is printed 2^(strlen(s)-1) times
# total = 1+2+....+2^(strlen(s)-1)
#       = (2^strlen(s)) - 1


#linked using recursion
