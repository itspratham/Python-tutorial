# 1. Fibonacci series
# def fib(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# print(fib(4))

# 2. A prime number

# def is_prime(n):
#     if n == 0:
#         return False
#     elif n == 1:
#         return False
#     for i in range(2, int(n / 2) + 1):
#         if n % i == 0:
#             return False
#     else:
#         return True
#
#
# f = []
# for i in range(10):
#     if is_prime(i):
#         f.append(i)
# print(f)

# 3. String Palindrome
# def is_palindrome(string):
#     f = ""
#     for i in range(len(string)):
#         f = f + string[len(string) - i-1]
#     return f
#
#
# print(is_palindrome("zagzag"))

# 4. Integer Palindrome
# def palindrome_integer(integer, a):
#     b = int(integer)
#     f = b % 10
#     ans = b // 10
#     if ans == 0:
#         return str(a) + str(f)
#     return palindrome_integer(str(ans), a + str(f))
#
#
# print(palindrome_integer("40360", ""))

# 5. Armstrong number
#
# 6. Avoiding deadlock in Java
#
# 7. Factorial
# def factorial(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))
# 8. Reverse a String

# 9. Remove duplicates from an array
# def remove_duplicates(arr):
#     count = 0
#     while count < len(arr):
#         if arr[count] in arr[count+1:]:
#             del arr[count]
#         count = count +1
#     return arr
# print(remove_duplicates([1,2,5,3,4,5,6,5]))
# 10. Printing patterns (solutions)
#
# 11. Print repeated characters of String?
#
# 12. GCD of two numbers
#
# 13. The square root of a number
#
# 14. Reverse array in place
#
# 15. Reverse words of a sentence
#
# 16. Leap year
#
# 17. Binary search
def binary_search(arr, target):
    sorted_list = sorted(arr)
    low = 0
    high = len(sorted_list) -1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return mid-1
    return mid


print(binary_search([2, 5, 4, 77, 7, 8, 70], 77))


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

# def merge_Sort(left, right):
#     i = 0
#     j = 0
#     result = []
#     # print(left, "left", "right", right)
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i = i + 1
#         else:
#             result.append(right[j])
#             j = j + 1
#     # print("left", left[i:])
#     result += left[i:]
#     # print("right", right[j:])
#     result += right[j:]
#     return result
#
#
# def merge_sort(lst):
#     if len(lst) <= 1:
#         return lst
#     mid = int(len(lst) / 2)
#     print(mid, "mid")
#     left = merge_sort(lst[:mid])
#     right = merge_sort(lst[mid:])
#     return merge_Sort(left, right)
#
#
# arr = [6, 3, 6, -1, 0, 98, 5, 87, 46]
# print(merge_sort(arr))


# def merge_Sort(left, right):
#     i, j = 0, 0
#     result = []
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i = i + 1
#         else:
#             result.append(right[j])
#             j = j + 1
#     result += left[i:]
#     result += right[j:]
#     return result
#
#
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = int(len(arr) / 2)
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = merge_Sort(left, right)
#     return result
#
#
# arr = [6, 3, 6, -1, 0, 98, 5, 87, 46]
# print(merge_sort(arr))

# Bubble Sort

# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i] < arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr
#
#
# print(bubble_sort([4, 2, 1, 47, 56, 99]))
