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

# num = input("Enter the number: ")
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

# string = "Great responsibility";
#
# print("Duplicate characters in a given string: ");
# # Counts each character present in the string
# for i in range(0, len(string)):
#     count = 1;
#     for j in range(i + 1, len(string)):
#         if (string[i] == string[j] and string[i] != ' '):
#             count = count + 1;
#             # Set string[j] to 0 to avoid printing visited character
#             string = string[:j] + '0' + string[j + 1:];
#
#             # A character is considered as duplicate if count is greater than 1
#     if (count > 1 and string[i] != '0'):
#         print(string[i])


# 12. GCD of two numbers
#
# Python Program to find GCD of Two Numbers

# num1 = float(input(" Please Enter the First Value  Num1 : "))
# num2 = float(input(" Please Enter the Second Value Num2 : "))
#
# a = num1
# b = num2
#
# while(num2 != 0):
#     temp = num2
#     num2 = num1 % num2
#     num1 = temp
#
# gcd = num1
# print("\n HCF of {0} and {1} = {2}".format(a, b, gcd))

# 13. The square root of a number

# def square_no(n):
#     import math
#     d = math.sqrt(n)
#     return d

# x = int(input('Enter a number : '))
# guess = 0.0 # The guess answer
# epsilon = 0.01 # Used for accuracy. See the condition in While Loop
# step = epsilon**2 #used to increment our guess 'ans'
# total_guesses = 0
# # We will understand this condition during code analysis
# while (abs(guess**2 - x)) >= epsilon:
#     guess += step
#     total_guesses += 1
#
# print('Total guesses were ' + str(total_guesses))
# if abs(guess**2-x) >= epsilon:
#     print('Failed on square root of ' + str(x))
# else:
#     print(str(guess) + ' is close to the square root of ' + str(x))

# 14. Reverse array in place

# def reverse_array(n):
#     array = []
#     for i in range((len(n)-1),-1,-1):
#         array.append(n[i])
#     return array
#
# print(reverse_array([323,24,2,32,42,3,23,24,4,2]))


# 15. Reverse words of a sentence

# def reversed_sentence(s):
#     t = []
#     for i in range(len(s)-1,-1,-1):
#         t.append(s[i])
#     return ''.join(t)
#
# print(reversed_sentence("hmfkdmf mdfm"))


# 16. Leap year
#
# 17. Binary search
# def binary_search(lists,x):
#     lists.sort()
#     mid = (len(lists) - 1)//2
#     if len(lists)>=1:
#         if x == lists[mid]:
#             return True
#
#         elif x < lists[mid]:
#             lists = lists[0:mid]
#             return binary_search(lists,x)
#
#         else:
#             lists = lists[mid+1:]
#             return binary_search(lists,x)
#     else:
#         return False
# a = list(map(int,input('enter list :').strip().split()))
# x = int(input('enter number for binary search : '))
#
# print(binary_search(a,x))

# 18. String Anagram
# str1="abcd"
# str2="bcad"
# word1=[]
# word2=[]
# for x in range(len(str1)):
#     word1.append(str1[x])
# for x in range(len(str2)):
#     word2.append(str2[x])
# if(len(word1)==len(word2)):
#     for letter in word1:
#         if letter in word2:
#             word2.remove(letter)
#
# if len(word2)==0:
#     print( "anagram")
# else:
#     print ("not anagram")
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
# def qsort(inlist):
#     if inlist==[]:
#         return []
#     else:
#         pivot = inlist[0]
#         lesser = qsort([x for x in inlist[1:] if x < pivot])
#         greater = qsort([x for x in inlist[1:] if x >= pivot])
#         return (lesser + [pivot] + greater)
#
# print(qsort([5,3,3,2,2,4,6,3]))


# 31. Insertion sort
#

# 32. Bubble sort
#
# 33. Transpose a matrix
#
# 34. Print all permutations of String
#
# from itertools import permutations
# perms = [''.join(p) for p in permutations('stack')]
# print(perms)
# print(len(perms))

# 35. Reverse a String in place
#
# 36. Adding two matrices in Java
#
# 37. Matrix multiplication
#
# 38. Removal all white space from String

# Python3 code to remove whitespace
# def remove(string):
#     return string.replace(" ", "")
#
#
# # Driver Program
# string = ' g e e k '
# print(remove(string))

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

# def counting_sort(l):
#     nums = l
#     highest = max(nums)+1
#     helper_list = [0] * highest
#     s_list = []
#     for i in range(len(nums)):
#         value = nums[i]
#         helper_list[value] += 1
#
#     for j in range(len(helper_list)):
#         s_list.append([j] * helper_list[j])
#
#     return s_list
# print(counting_sort([5,4,32,2,4,4,5,6,6,3,3,0]))
#
# 48. Check if two string rotation of each other


# Python program to check if strings are rotations of
# each other or not

# Function checks if passed strings (str1 and str2)
# are rotations of each other
# def areRotations(string1, string2):
#     size1 = len(string1)
#     size2 = len(string2)
#     temp = ''
#
#     # Check if sizes of two strings are same
#     if size1 != size2:
#         return 0
#
#     # Create a temp string with value str1.str1
#     temp = string1 + string1
#
#     # Now check if str2 is a substring of temp
#     # string.count returns the number of occurrences of
#     # the second string in temp
#     if (temp.count(string2) > 0):
#         return 1
#     else:
#         return 0
#
#
# # Driver program to test the above function
# string1 = "AACD"
# string2 = "ACDE"
#
# if areRotations(string1, string2):
#     print("Strings are rotations of each other")
# else:
#     print("Strings are not rotations of each other")

# This code is contributed by Bhavya Jain


# 50. Merge sort



# def merge_sort(x):
#
#     if len(x) < 2:
#         return x
#
#     result,mid = [],int(len(x)/2)
#
#     y = merge_sort(x[:mid])
#     z = merge_sort(x[mid:])
#
#     while (len(y) > 0) and (len(z) > 0):
#             if y[0] > z[0]:
#                 result.append(z.pop(0))
#             else:
#                 result.append(y.pop(0))
#
#     result.extend(y+z)
#     return result
#
# print(merge_sort([4,32,4,5,6,4,334,43]))
''']'
def pattern_match(string1,string2):
    for i in range(len(string1)):
        for j in range(len(string2)):
            if string2[:] == string1[j:i+1]:
                print(f"it is at {j+1}th position")

    return
pattern_match("funcuncle","funcun")
'''


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node= self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def insert_at_pos(self,pos,data):
        new_node = Node(data)
        if self.head is None and pos<=0:
            self.append(data)
            return
        if self.head.next is None and pos==1:
            new_node.next = self.head
            self.head = new_node
        prev = self.head
        count = 2
        while pos != count:
           count += 1
           prev = prev.next
        new_node.next = prev.next
        prev.next = new_node


    def print_list(self):
        last_node = self.head
        while last_node:
            print(last_node.data)
            last_node = last_node.next

    def delete_node(self,key):
        if self.head.data is None:
            print("No scope to delete the node")
        curr_node = self.head
        if curr_node and curr_node.data==key:
            self.head = curr_node.next
            curr_node = None

        prev = None
        while curr_node.data and curr_node.data !=key:
             prev = curr_node
             curr_node = curr_node.next

        prev.next = curr_node.next
        curr_node = None

    def delete_at_position(self,pos):
        cur_node = self.head
        if self.head.data is None or pos<=0:
            print("List is empty or invalid position given")
            return
        if pos==1:
            self.head = self.head.next
            return
        count = 1
        prev = None
        while count!=pos:
            prev= cur_node
            cur_node = cur_node.next
            count = count+1
        prev.next = cur_node.next
        cur_node =None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse_string(self):
        prev = None
        headd =self.head
        currnode = self.head
        while currnode:
            #make a temporary next node
            nxt = currnode.next
            currnode.next = prev
            prev = currnode
            currnode = nxt
        self.head = prev
        headd.next = None


    def ispalindrome(self):
        pass

    def length(self):
        if self.head is None:
            return 0
        curnode = self.head
        count = 1
        while curnode.next:
            curnode = curnode.next
            count =count + 1

        return count



l = LinkedList()
l.append("A")
l.append("B")
l.append("C")
l.append("D")
l.append("E")
l.reverse_string()
l.print_list()
print(l.length())