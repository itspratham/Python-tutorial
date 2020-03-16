# 1. Fibonacci series

# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return int(fib(n-1)+fib(n-2))
#
#
# print(fib(4))


# 2. A prime number


# num = int(input("Enter a number: "))
#
# if num > 1:
# 	for i in range(2, num):
# 		if (num % i) == 0:
# 			print(num, "is not a prime number")
# 			print(i, "times", num // i, "is", num)
# 			break
# 	else:
# 		print(num, "is a prime number")
#
# else:
# 	print(num, "is not a prime number")


# 3. String Palindrome

# def palindrome(n):
#     for i in range(len(n)):
#         if n[i] == n[len(n)-i-1]:
#             print("It is a palindrome")
#             break
#     else:
#             print("It is not a palindrome")
# palindrome("malyalam")

# 4. Integer Palindrome

# num = input("Enter the number")
# num = int(num)
# def reverse(num):
#   rev = 0
#   while num > 0:
#     rev = (10*rev) + num%10
#     num //= 10
#   return rev
#
# print(num)
# if num == reverse(num):
#     print("IT is a palindrome")
# else:
#     print("It is not a palindrome")

# 5. Armstrong number

# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153
#
# Input : 120
# Output : No
# 120 is not a Armstrong number.
# 1*1*1 + 2*2*2 + 0*0*0 = 9
#
# Input : 1253
# Output : No
# 1253 is not a Armstrong Number
# 1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723
#
# Input : 1634
# Output : Yes
# 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634


# Function to calculate x raised to the power y
# def power(x, y):
# 	if y==0:
# 		return 1
# 	if y%2==0:
# 		return power(x, y/2)*power(x, y/2)
# 	return x*power(x, y/2)*power(x, y/2)
#
# # Function to calculate order of the number
# def order(x):
#
# 	# variable to store of the number
# 	n = 0
# 	while (x!=0):
# 		n = n+1
# 		x = x/10
# 	return n
#
# # Function to check whether the given number is
# # Armstrong number or not
#
# def isArmstrong (x):
# 	n = order(x)
# 	temp = x
# 	sum1 = 0
# 	while (temp!=0):
# 		r = temp%10
# 		sum1 = sum1 + power(r, n)
# 		temp = temp/10
#
# 	# If condition satisfies
# 	return (sum1 == x)
#
#
# # Driver Program
# x = 153
# print(isArmstrong(x))
# x = 1253
# print(isArmstrong(x))



# 6. Avoiding deadlock in Java


#**********************#
#**********************#






# 7. Factorial

# def fact(n):
#     if n == 0 and 1:
#         return 1
#     else:
#         return fact(n-1) * n
#
# print(fact(6))

# 8. Reverse a String

# def reversed_string(string):
#     temp =[]
#     for i in range(len(string)):
#         temp.append(string[len(string)-i-1])
#
#     return ''.join(temp)
# print(reversed_string("jack"))


# 9. Remove duplicates from an array

# myList = [1, 2, 3, 1, 2, 5, 6, 7, 8]
# cleanlist = []
# [cleanlist.append(x) for x in myList if x not in cleanlist]
# print(cleanlist)

# 10. Printing patterns (solutions)
#
# 11. Print repeated characters of String?
#
# 12. GCD of two numbers
#
# 13. The square root of a number

# def square_no(n):
#     import math
#     d = math.sqrt(n)
#     return d

x = int(input('Enter a number : '))
guess = 0.0 # The guess answer
epsilon = 0.01 # Used for accuracy. See the condition in While Loop
step = epsilon**2 #used to increment our guess 'ans'
total_guesses = 0
# We will understand this condition during code analysis
while (abs(guess**2 - x)) >= epsilon:
    guess += step
    total_guesses += 1

print('Total guesses were ' + str(total_guesses))
if abs(guess**2-x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print(str(guess) + ' is close to the square root of ' + str(x))

# 14. Reverse array in place
#
# 15. Reverse words of a sentence
#
# 16. Leap year
#
# 17. Binary search
#
# 18. String Anagram
#
# 19. Design a Vending Machine
#
# 20. Reverse a number
#
# 21. The first non-repeated character of String
#
# 22. Finding Middle element of linked list in one pass
#
# 23. Pre-order traversal
#
# 24. Pre-order traversal without recursion
#
# 25. In order traversal
#
# 26. In order traversal without recursion
#
# 27. Post-order traversal
#
# 28. Postorder traversal without recursion
#
# 29. Print all leaves of a binary tree
#
# 30. Sort array using quicksort
#
# 31. Insertion sort
#
# 32. Bubble sort
#
# 33. Transpose a matrix
#
# 34. Print all permutations of String
#
# 35. Reverse a String in place
#
# 36. Adding two matrices in Java
#
# 37. Matrix multiplication
#
# 38. Removal all white space from String
#
# 39. Reverse a linked list
#
# 40. Find the length of the linked list
#
# 41. Check if a linked list has a loop
#
# 42. Find the start of loop in a linked list
#
# 43. Find the middle element of a linked list
#
# 44. Find the 3rd element from the tail linked list
#
# 44. Convert a linked list to a binary tree
#
# 45. Sort a linked list
#
# 46. Iterative Quicksort
#
# 46. Bucket sort
#
# 47. Counting sort
#
# 48. Check if two string rotation of each other
#
# 49. LRU cache in Java
#
# 50. Merge sort
