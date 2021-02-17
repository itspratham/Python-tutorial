# # Given an unsorted array arr[] of size N, rotate it by D elements (clockwise).
# #
# # Input:
# # The first line of the input contains T denoting the number of testcases.
# # First line of each test case contains two space separated elements,
# # N denoting the size of the array and an integer D denoting the number size of the rotation.
# # Subsequent line will be the N space separated array elements.
# #
# # Output:
# # For each testcase, in a new line, output the rotated array.
# #
# # Constraints:
# # 1 <= T <= 200
# # 1 <= N <= 107
# # 1 <= D <= N
# # 0 <= arr[i] <= 105
# #
# # Example:
# # Input:
# # 2
# # 5 2
# # 1 2 3 4 5
# # 10 3
# # 2 4 6 8 10 12 14 16 18 20
# #
# # Output:
# # 3 4 5 1 2
# # 8 10 12 14 16 18 20 2 4 6
# #
# # Explanation :
# # Testcase 1: 1 2 3 4 5  when rotated by 2 elements, it becomes 3 4 5 1 2.
#
# def rotate(n,rot,arr):
#     for i in range(n-rot):
#         f = arr.pop()
#         arr.insert(0,f)
#     return arr
#
# def main():
#     n = int(input("Enter the no of arrays to be rotated: "))
#     for i in range(n):
#         no = list(map(int, input("enter the length and by integer it has to be roated: ").split()))
#         arr = list(map(int, input("enter the array: ").split()))
#         arr_d = arr.copy()
#         v = rotate(no[0],no[1],arr)
#         print("Original array: ",arr_d)
#         print("Rotated array: ",v)
#
# main()


# Given an array arr[] and a number K where K is smaller than size of array,
# the task is to find the Kth smallest element in the given array.
# It is given that all array elements are distinct.
#
# Input:
# The first line of input contains an integer T, denoting the number of testcases. Then T test cases follow. Each test case consists of three lines. First line of each testcase contains an integer N denoting size of the array. Second line contains N space separated integer denoting elements of the array. Third line of the test case contains an integer K.
#
# Output:
# Corresponding to each test case, print the kth smallest element in a new line.
#
# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 105
# 1 <= arr[i] <= 105
# 1 <= K <= N
#
# Example:
# Input:
# 2
# 6
# 7 10 4 3 20 15
# 3
# 5
# 7 10 4 20 15
# 4
# Output:
# 7
# 15
#
# Explanation:
# Testcase 1: 3rd smallest element in the given array is 7.
# Testcase 2: 4th smallest elements in the given array is 15.


# def smallest(arr,k):
#     arr = sorted(arr)
#     return arr[k-1]
#
# print(smallest([2,3,4,5,6],2))


# Nth number made of prime digits

# Rotate a 2D array without using extra space

# def rotate(l):
#     new_l = []
#     b = 0
#     for _ in range(1, 4):
#         temp = []
#         a = 2
#         for _ in range(1, 4):
#             temp.append(l[a][b])
#             a = a - 1
#
#         new_l.append(temp)
#         b = b + 1
#
#     return new_l.copy()
#
#
# l = rotate(l)
#
# for i in range(len(l)):
#     for j in range(len(l)):
#         print(str(l[i][j]), end=" ")
#     print()


# Greater on right side
# Input:
# 2
# 6
# 16 17 4 3 5 2
# 4
# 2 3 1 9
#
# Output:
# 17 5 5 5 2 -1
# 9 9 9 -1
#
# Explanation:
# Testcase1: For 16 the greatest element on its right is 17.
# For 17 it's 5. For 4 it's 5.
# For 3 it's 5. For 5 it's 2.
# For 2 it's -1(no element to its right).
# So the answer is 17 5 5 2 -1

# def greater(arr,b):
#     arr1 = []
#     for i in range(len(arr)-1):
#         print(max(arr[i+1:]))
#         arr1.append(max(arr[i+1:]))
#     arr1.append(-1)
#     return arr1
#
# def main():
#     n = int(input("Enter the testcase number: "))
#     for i in range(n):
#         b = int(input("Enter the length: "))
#         arr = list(map(int,input("Enter the array: ").split()))
#         f = greater(arr,b)
#         print(f)

# main()

# Replace all 0's with 5
# Example:
# Sample Input:
# 2
# 1004
# 121
#
# Sample Output:
# 1554
# 121
#
# Explanation:
# Test Case 1: There are two zeroes in "1004", on replacing all zeroes with "5",
# the new number will be "1554".
# Test Case 2: Since there are no zeroes in "121", the number remains as "121".

# def reaplce(strr):
#     c  = ""
#     for i in range(len(strr)):
#         if strr[i] == "0":
#             c = c + "5"
#         else:
#             c = c+strr[i]
#     return c
#
# print(reaplce("1201000"))


# Game with nos
# Constraints:
#
# 1<=t<=100
#
# 1<=n<=100000
#
# 1<=A[i]<=100000
#
# Example:
#
# Sample Input 0
# 1
# 5
# 10 11 1 2 3
#
# Sample Output 0
# 1 10 3 1 3

# def game(arr):
#     arr1 =[]
#     for i in range(len(arr)-1):
#         arr1.append(arr[i] ^ arr[i+1])
#     arr1.append(arr[-1])
#     return arr1
# print(game([10,11, 1, 2, 3]))


# Reverse array in groups
# Input
# 4
# 5 3
# 1 2 3 4 5
# 4 3
# 5 6 8 9
# 4 7
# 5 6 8 9
# 8 3
# 1 2 3 4 5 6 7 8
#
# Output
# 3 2 1 5 4
# 8 6 5 9
# 9 8 6 5
# 3 2 1 6 5 4 8 7
#
# Explanation:
# Testcase 1: Reversing groups in size k = 3, first group consists of elements 1, 2, 3.
# Reversing this group, we have elements in order as 3, 2, 1.
# Testcase 2: Our array is 5 6 8 9. The value of k is 3. So we reverse it in groups of 3.
# After reversing, it becomes 8 6 5 9.
# Testcase 3: Our array is 5 6 8 9. The value of k is 7. After reversing, it becomes 9 8 6 5.
# Testcase 4: Our array is 1 2 3 4 5 6 7 8. The value of k is 3.
# After reversing, it becomes 3 2 1 6 5 4 8 7.

# def rev(arr,k):
#     arr1 = []
#     n = len(arr) - k

# Count pairs with given sum
# Example:
# Input
# 2
# 4 6
# 1  5  7 1
# 4 2
# 1 1 1 1
# Output
# 2
# 6

# def function(arr,k):
#     count =0
#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             if arr[i] + arr[j] == k:
#                 count = count +1
#     return count
#
# print(function([1,5,7,1],6))


import operator


# Find Missing And Repeating
# def misising(arr):
#     d = dict()
#     l = []
#     for i in range(len(arr)):
#         if arr[i] in l:
#             d[arr[i]] = d[arr[i]] + 1
#         else:
#             d[arr[i]] = 1
#         l.append(arr[i])
#     inverse = [(value, key) for key, value in d.items()]
#     d = list(set(arr))
#     n = max(d)
#     for i in range(1,n):
#         if i not in d:
#             return max(inverse)[1], i
#         else:
#             return max(inverse)[1], min(d)
# print(misising([3,4,6,3,4,4,1,5,5,5,5,5,5,2,1]))


# Non-Repeating Element


# def nonrepeat(arr):
#     d = dict()
#     l = []
#     for i in range(len(arr)):
#         if arr[i] in l:
#             d[arr[i]] = d[arr[i]] + 1
#         else:
#             d[arr[i]] = 1
#         l.append(arr[i])
#     inverse = [(value, key) for key, value in d.items()]
#     return min(inverse)[1]
#
# print(nonrepeat([9 ,4, 9, 6 ,7 ,4]))


# Find the smallest and second smallest element in an array
# Input :
# 3
# 5
# 2 4 3 5 6
# 6
# 1 2 1 3 6 7
# 2
# 1 1
# Output :
# 2 3
# 1 2
# -1

# def smallest(arr):
#     first = arr[0]
#     second = arr[1]
#     for i in range(0, len(arr)):
#
#         # If current element is smaller than first then
#         # update both first and second
#         if arr[i] < first:
#             second = first
#             first = arr[i]
#
#             # If arr[i] is in between first and second then
#         # update second
#         elif (arr[i] < second and arr[i] != first):
#             second = arr[i];
#
#     return first,second
#
# print(smallest([-1,2,3, 12, 13, 1, 10, 34, 1]))


# ugly numbers

# def maxDivide( a, b ):
# 	while a % b == 0:
# 		a = a / b
# 	return a
#
# # Function to check if a number
# # is ugly or not
# def isUgly( no ):
# 	no = maxDivide(no, 2)
# 	no = maxDivide(no, 3)
# 	no = maxDivide(no, 5)
# 	return 1 if no == 1 else 0
#
# # Function to get the nth ugly number
# def getNthUglyNo( n ):
# 	i = 1
# 	count = 1 # ugly number count
#
# 	# Check for all integers untill
# 	# ugly count becomes n
# 	while n > count:
# 		i += 1
# 		if isUgly(i):
# 			count += 1
# 	return i
#
# # Driver code to test above functions
# no = getNthUglyNo(10)
# print("the ugly no. is ", no)


# Implement Queue using array

# class Queue:
# 	def __init__(self, arr = []):
# 		self.arr = arr
#
# 	def enqueue(self,value):
# 		if value not in self.arr:
# 			self.arr.insert(0,value)
# 			print(f"The value has been enqueued into the queue {value}")
# 		else:
# 			print(f"the value is already there in the queue")
#
# 	def dequeue(self,value):
# 		element = 0
# 		if value in self.arr:
# 			while element != value:
# 				element = self.arr.pop(0)
# 				print(f"Popped element is {element}")
#
# 			#self.arr.remove(value)
# 			print(f"The {value} has been dequeued.")
# 		else:
# 			print(f"The value is not present. Dequeue something else: \nhere is the queue {self.arr}")
#
# 	def print_queue(self):
# 		if self.arr == []:
# 			print("Enqueue some numbers ")
# 		else:
# 			print(self.arr)
#
#
#
# v = Queue()
# v.enqueue(3)
# v.enqueue(5)
# v.print_queue()
# v.dequeue(6)
# v.enqueue(3)
# v.dequeue(3)
#
# v.print_queue()

# Stock buy and sell
# Example
# Input:
# 3
# 7
# 100 180 260 310 40 535 695
# 4
# 100 50 30 20
# 10
# 23 13 25 29 33 19 34 45 65 67
#
# Output:
# (0 3) (4 6)
# No Profit
# (1 4) (5 9)

# def buyandsell(arr):
#     d = dict()
#     maxx =0
#     for i in range(len(arr)):
#         for j in range(i +1, len(arr)):
#             if abs(arr[j] -arr[i]) > maxx:
#                 maxx = abs(arr[j] -arr[i])
#     return maxx
#
# print(buyandsell([100, 180, 260 ,310, 40, 535, 695]))

def subarraySum(nums, k):
    l = [0]
    g = 0
    for num in nums:
        g = g + num
        l.append(g)
    count = 0
    l1 = []
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if abs(l[i] - l[j]) == k:
                l1.append(nums[i:j])
                count = count + 1
    print(l1)
    return l


#
#
# print(subarraySum(nums=[1,2,3,4,2,6,2,4,2], k=8))
#


# Smallest subarray with sum greater than x
# Examples:
# A[] = {1, 4, 45, 6, 0, 19}
#    x  =  51
# Output: 3
# Minimum length subarray is {4, 45, 6}
#
# A[] = {1, 10, 5, 2, 7}
#    x  = 9
# Output: 1
# Minimum length subarray is {10}


# def subarray(arr,k):
#     g = 0
#     l = [0]
#     d = dict()
#     for i in range(len(arr)):
#         g = g + arr[i]
#         l.append(g)
#     for i in range(1,len(l)):
#         for j in range(i+1, len(l)):
#             if abs(l[i] - l[j]) > k:
#                 d[tuple(arr[i:j])] = abs(l[i] - l[j])
#
#     g = [(values,key) for key,values in d.items()]
#     print("Output is: ",len(d))
#     print(min(g)[1])
#
# subarray([1, 10, 5, 2, 7],9)


# Wave Array
# Input:
# 1
# 5
# 1 2 3 4 5
# Output:
# 2 1 4 3 5
#
# Explanation:
# Testcase 1: Array elements after sorting it in wave form are 2 1 4 3 5.

# def wave(arr):
#     for i in range(0,len(arr)-1,2):
#             arr[i], arr[i+1] = arr[i+1],arr[i]
#     return arr
# print(wave([1,2,3,4,5]))


# Python function to sort the array arr[0..n-1] in wave form,
# i.e., arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= arr[5]
# def sortInWave(arr, n):
#     # Traverse all even elements
#     for i in range(0, n, 2):
#
#         # If current even element is smaller than previous
#         if (i > 0 and arr[i] < arr[i - 1]):
#             arr[i], arr[i - 1] = arr[i - 1], arr[i]
#
#         # If current even element is smaller than next
#         if (i < n - 1 and arr[i] < arr[i + 1]):
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]
#
#         # Driver program
#
#
# arr =[1,2,3,4,5]
# sortInWave(arr, len(arr))
# for i in range(0, len(arr)):
#     print(arr[i],)

# Kth smallest element
# Input:
# 2
# 6
# 7 10 4 3 20 15
# 3
# 5
# 7 10 4 20 15
# 4
# Output:
# 7
# 15
#
# Explanation:
# Testcase 1: 3rd smallest element in the given array is 7.
# Testcase 2: 4th smallest elemets in the given array is 15.

# def smallest(arr,k):
#     arr.sort()
#     return arr[k-1]
#
# print(smallest([1,2,3,4,5,6],6))


# Sum of array elements
# Example:
# Input:
# 2
# 3
# 3 2 1
# 4
# 1 2 3 4
# Output:
# 6
# 10

# def summ(arr):
#     g = 0
#     for i in range(len(arr)):
#         g = g+ arr[i]
#     return g
#
# print(summ([1,2,3,4]))


# Sum of f(a[i], a[j]) over all pairs in an array of n integers

# def sum_of_All_pairs(arr):
#     g = 0
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[j]-arr[i]:
#                 g = g + (arr[j] - arr[i])
#     return g
#
# print(sum_of_All_pairs([6,6,4,4]))


# Sherlock a Detective
# def sherlock(a,k):
#     l = range(0,k+ 1)
#     gh =[]
#     for i in l:
#         if i not in a:
#             gh.append(i)
#     return gh
#
# print(sherlock([0,1,1,2,2,3],6))


# Ishaan Loves Chocolates
# As we know, Ishaan has a love for chocolates.
# He has bought a huge chocolate bar which contains N chocolate squares.
# Each of the square has a tastiness level which is denoted by an array A[].
# Ishaan can eat the first or the last square of the chocolate at once.
# Ishaan has a sister who loves chocolates too and she demands the last chocolate square.
# Now, Ishaan being greedy eats the more tasty square first.
# Determine the tastiness level of the square which his sister gets.
#
# Input :
# First line of input contains a single integer T denoting the number of test cases.
# The first line of each test case contains an integer N.
# The second line contains N space-separated integers denoting the array A.
#
# Output :
# For each test case, print the required answer in a new line.
#
# Constraints :
# 1 <= T <= 100
# 1 <= N <= 250
# 1 <= A[i] <= 1000
#
# Example :
# Input :
# 3
# 5
# 5 3 1 6 9
# 6
# 2 6 4 8 1 6
# 4
# 2 2 2 2
# Output :
# 1
# 1
# 2
#
# Explaination :
# Case 1 :
# Initially : 5 3 1 6 9
# 5 3 1 6
# 5 3 1
# 3 1
# 1
#
# Case 2 :
# Initially : 2 6 4 8 1 6
# 2 6 4 8 1
# 6 4 8 1
# 4 8 1
# 8 1
# 1
#
# Case 3 :
# Initially : 2 2 2 2
# 2 2 2
# 2 2
# 2

# def chocolate(arr):
#     i = 0
#     while len(arr)!=1:
#         if arr[0] >= arr[-1]:
#             arr.pop(0)
#         else:
#             arr.pop(-1)
#         i = i+1
#     return arr[0]

# print(chocolate([2 ,6, 4 ,8, 1, 6]))

# Distinct absolute array elements
# Input:
# 3
# 4
# -35 73 73 73
# 9
# -44 -31 -6 6 46 52 52 55 93
# 6
# -3 -2 0 3 4 5
#
#
# Output:
# 2
# 7
# 5

# def distinct(arr):
#     d = {}
#     for i in range(len(arr)):
#         d[abs(arr[i])] = 1
#     return sum(d.values())
#
# print(distinct([-44 ,-31, -6 ,6 ,46 ,52, 52, 55, 93]))
# print(distinct([-3 ,-2, 0, 3, 4 ,5]))


# Inverse Permutation
# Example:
# Input:
# 3
# 4
# 1 4 3 2
# 5
# 2 3 4 5 1
# 5
# 2 3 1 5 4
#
# Output:
# 1 4 3 2
# 5 1 2 3 4
# 3 1 2 5 4


# def inversePermutation(arr, size):
#     # Loop to select Elements one by one
#     for i in range(0, size):
#         for j in range(0, size):
#             if (arr[j] == i + 1):
#                 # print position of element where
#                 # element is in inverse permutation
#                 print(j + 1, end=" ")
#                 break
#
# inversePermutation([2, 3, 4, 5, 1],5)


# Testing for the internet

# import urllib.request
#
# def connect(host='http://google.com'):
#     try:
#         urllib.request.urlopen(host) #Python 3.x
#         return True
#     except:
#         return False
#
# print( "connected" if connect() else 'no internet!' )

# Multiply Array

# def multiply(arr):
#     d =1
#     for i in range(len(arr)):
#         d = d * arr[i]
#     return d
#
# print(multiply([5,5,5,5,5,5,5,5,5,5]))


# Count Pairs in an Array
# Example:
#
# Input: arr[] = {5, 0, 10, 2, 4, 1, 6}
#
# Output: 5
#
# Explanation:
# Pairs which hold condition i*arr[i] > j*arr[j] are
# (10, 2) (10, 4) (10, 1) (2, 1) (4, 1)

# def count_pairs(arr):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i] * i >j * arr[j]:
#                 print(arr[i],arr[j])
#                 count = count +1
#     print(count)
#
# count_pairs([5, 0, 10, 2, 4, 1, 6])


# Convert array into Zig-Zag fashion

# def zigzag(arr):
#     i = 0
#     flag = 0
#     while i < len(arr)-1:
#         if flag == 0:
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1],arr[i]
#         elif flag == 1:
#             if arr[i] < arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1],arr[i]
#         i = i +1
#
#         flag = not(flag)
#     return arr
# # print(zigzag([4 ,3 ,7, 8 ,6 ,2 ,1]))
# print(zigzag([1,4,3,2]))


# Find the fine
# def fine():
#     month_day = list(map(int,input("Enter the day and month: ").split()))
#     gaari_no = list(map(int,input("Enter the vehicle numbers: ").split()))
#     fines = list(map(int,input("Enter the fines for the vehicles: ").split()))
#     temp = 0
#     if month_day[1] % 2 == 0:
#         for i in range(len(gaari_no)):
#             if gaari_no[i] % 2 == 1:
#                 temp = temp + fines[i]
#     elif month_day[1] % 2 == 1:
#         for i in range(len(gaari_no)):
#             if gaari_no[i] % 2 == 0:
#                 temp = temp + fines[i]
#
#     return temp
# print(fine())


# Max sum in the configuration

# Input
# 1
# 4
# 8 3 1 2
# Output
# 29

# def maxsum(arr):
#     l = []
#     for _ in range(len(arr)):
#         f = arr.pop(0)
#         arr.append(f)
#         g = 0
#         for j in range(len(arr)):
#             g = g + arr[j]*j
#         l.append(g)
#     return max(l)
#
# print(maxsum([8, 3 ,1 ,2]))


# Merge Without Extra Space
# Input:
# 2
# 4 5
# 1 3 5 7
# 0 2 6 8 9
# 2 3
# 10 12
# 5 18 20
#
# Output:
# 0 1 2 3 5 6 7 8 9
# 5 10 12 18 20

# def merger(arr1,arr2):
#     arr3 = arr1+ arr2
#     arr3.sort()
#     return arr3
#
# print(merger([1, 3 ,5 ,7],[0 ,2 ,6, 8 ,9]))
#


# Count the subarrays having product less than k
# def subarray_mul(arr,k):
#     l = []
#     h = 1
#     for i in range(len(arr)):
#         h = h * arr[i]
#         l.append(h)
#     l1 = []
#     count = 0
#     for i in range(len(l)):
#         for j in range(i+1, len(l)):
#             if l[i] // l[j] < k:
#                 l1.append(arr[i:j])
#                 count = count + 1
#     return l1, count
#
# print(subarray_mul([1,2,3,4],10))


# Python3 program to count subarrays
# having product less than k.

# def countsubarray(array, n, k):
#     count = 0
#     for i in range(0, n):
#         if array[i] <= k:
#             count += 1
#         mul = array[i]
#
#         for j in range(i + 1, n):
#             mul = mul * array[j]
#             if mul <= k:
#                 count += 1
#     return count
#
# array = [1, 2, 3, 4]
# k = 10
# size = len(array)
# count = countsubarray(array, size, k);
# print(count, end=" ")


# Minimum number to make median X

# Max Circular Subarray Sum

# def ciruclar_sum(arr):
#     d = {}
#     for i in range(len(arr)):
#         summ = 0
#         for j in range(len(arr)-1):
#             summ = summ + arr[j]
#         d[tuple(arr)] = summ
#         p = arr.pop(0)
#         arr.append(p)
#     d = [(values, keys) for keys, values in d.items()]
#
#     return max(d)[0], max(d)[1]
#     #return d
#
# print([ciruclar_sum([-1 ,40, -14, 7 ,6 ,5, -4, -1])])
#
# print([ciruclar_sum([10 ,-3, -4, 7, 6 ,5 ,-4, -1])])


# Ugly Numbers

# def maxDivide( a, b ):
# 	while a % b == 0:
# 		a = a / b
# 	return a
#
# def isUgly( no ):
# 	no = maxDivide(no, 2)
# 	no = maxDivide(no, 3)
# 	no = maxDivide(no, 5)
# 	return 1 if no == 1 else 0
#
# # Function to get the nth ugly number
# def getNthUglyNo( n ):
# 	i = 1
# 	count = 1 # ugly number count
# 	while n > count:
# 		i += 1
# 		if isUgly(i):
# 			count += 1
# 	return i
#
#
# no = getNthUglyNo(int(input("Enter the no: ")))
# print("150th ugly no. is ", no)


# Linked List
# class Node:
#     def __init__(self,data):
#         self.data =data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self,data):
#         node_data = Node(data)
#         node = self.head
#         if self.head is None:
#             self.head = node_data
#         else:
#             while node.next is not None:
#                 node = node.next
#             node.next = node_data
#
#     def delete_a_node(self,data):
#         node = self.head
#         if self.head.data == data:
#             self.head.next = self.head
#             node.next = None
#
#
#     def print_linkedlist(self):
#         while self.head is not None:
#             print(self.head.data)
#             self.head = self.head.next
#
# f = LinkedList()
# f.append(9)
# f.append(8)
# f.append(7)
# f.append(6)
# f.delete_a_node(9)
# f.print_linkedlist()


import re


def longestSubstring(str):
    letter = max(re.findall(r'\D+', str), key=len)
    digit = max(re.findall(r'\d+', str), key=len)

    return letter, digit


# Driver Code
str = 'geeks23geeksforgeeks1'
print(longestSubstring(str))
