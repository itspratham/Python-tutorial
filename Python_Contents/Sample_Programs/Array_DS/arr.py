# Write a Python program to find the first duplicate element
# in a given array of integers.
# Return -1 If there are no such elements.
#
# def prog(arr):
#     for  i in range(len(arr)-1):
#         for j in range(1,len(arr)):
#             if arr[i] == arr[j]:
#                 return arr[i]
#
# print(prog([4,3,4,5,2,4,3]))

# def find_first_duplicate(nums):
#     num_set = set()
#     no_duplicate = -1
#
#     for i in range(len(nums)):
#
#         if nums[i] in num_set:
#             return nums[i]
#         else:
#             num_set.add(nums[i])
#
#     return no_duplicate
#
# print(find_first_duplicate([1, 2, 3, 4, 4, 5]))
# print(find_first_duplicate([1, 2, 3, 4]))
# print(find_first_duplicate([1, 1, 2, 3, 3, 2, 2]))


# Write a Python program to find whether a given array
# of integers contains any duplicate element.
# Return true if any value appears at least twice in the said array
# and return false if every element is distinct.

# def prog(arr):
#     for  i in range(len(arr)-1):
#         for j in range(1,len(arr)):
#             if arr[i] == arr[j]:
#                 return True
#     return False
#
# print(prog([4,3,4,5,2,4,3]))

# def test_duplicate(array_nums):
#     nums_set = set(array_nums)
#     return len(array_nums) != len(nums_set)
# print(test_duplicate([1,2,3,4,5]))
# print(test_duplicate([1,2,3,4, 4]))
# print(test_duplicate([1,1,2,2,3,3,4,4,5]))

# Write a Python program to convert an array to an ordinary list with the same items.

# from array import *
# array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# print("Original array: "+str(array_num))
# num_list = array_num.tolist()
# print("Convert the said array to an ordinary list with the same items:")
# print(num_list)

# Write a Python program to remove the first occurrence of a specified element from an array.
# l = [1,3,4,5,3,5]
# l.remove(5)
# print(l)

# n= 5
# for i in range(len(l)):
#     if l[i]== n:
#         l.remove(l[i])
#         break
# print(l)


# Write a Python program to remove a specified item using the index from an array.
# from array import *
# array_num = array('i', [1, 3, 5, 7, 9])
# print("Original array: "+str(array_num))
# print("Remove the third item form the array:")
# array_num.pop(2)
# print("New array: "+str(array_num))


# 1. Write a python program to sort a numeric array and a string array.
# 

# 
# 2. Write a python program to sum values of an array. 
# 
# 
# 
# 3. Write a python program to print the following grid.

# Expected Output :
# 
# - - - - - - - - - -                                                                                           
# - - - - - - - - - -                                                                                           
# - - - - - - - - - -                                                                                           
# - - - - - - - - - -                                                                                           
# - - - - - - - - - -                                                                                           
# - - - - - - - - - -                                                                                           
# - - - - - - - - - -                                                                                           
# - - - - - - - - - -                                                                                           
# - - - - - - - - - -                                                                                           
# - - - - - - - - - -  


# for i in range(10):
#     for j in range(10):
#         print("-",end=" ")
#     print()


# 4. Write a python program to calculate the average value of array elements.

# def arrayy(Arr):
#     n =len(Arr)
#     x =sum(Arr)
#     print(x/n)
# arrayy([6,4,3,2,5,6,4,1,1,2,1,1])


# 5. Write a python program to test if an array contains a specific value. 

# def arrayy(arr,specific):
#     if specific in arr:
#         return True
#     return False
# print(arrayy([3,4,5,4,3,2,4,4],5))

# 6. Write a python program to find the index of an array element. 

# def index(arr,element):
#     for i in range(len(arr)):
#         if arr[i] == element:
#             return i+1
# print(index([3,1,2,5,7,10],10))


# 7. Write a python program to remove a specific element from an array.

# def specific_pgm(array,specific):
#     for i in range(len(array)):
#         if array[i] == specific:
#             array.remove(array[i])
#             break
#     return array
# print(specific_pgm([2,3,4,2,5,6,7],2))


# 8. Write a python program to copy an array by iterating the array. 

# def arr_iter(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         new_arr.append(arr[i])
#     return new_arr
#
# print(arr_iter([3,4,5,6,7,3,7]))


# 9. Write a python program to insert an element (specific position) into an array.

# def arary(arr,specific,data):
#     arr.insert(specific,data)
#     return arr
# print(arary([2,4,2,1,5,6,7],4,9))


# 10. Write a python program to find the maximum and minimum value of an array.

# def max_min(arr):
#     min =arr[0]
#     max = arr[1]
#     for i in range(len(arr)):
#         if max> arr[i]:
#             min = arr[i]
#         else:
#             max = arr[i]
#     print("min:" ,min)
#     print("Max:",max)
#
# max_min([5,3,7,2,9,1])


# 11. Write a python program to reverse an array of integer values. 

# def reve(my_array1):
#     for i in range(len(my_array1)//2):
#         my_array1[i] ,my_array1[len(my_array1)- i - 1]= my_array1[len(my_array1)- i - 1],\
#                                                         my_array1[i];
#
#     return my_array1
# print(reve([2,34,4,5,6,7,54,3,2,2,4,4]))


# 12. Write a python program to find the duplicate values of an array of integer values.

# def duplicate(arr):
#     new = []
#     for i in range(len(arr)):
#         if arr[i] in arr[i+1:]:
#             new.append(arr[i])
#     return new
#
# print(duplicate([2,6,4,3,2,8,4,6]))


# 13. Write a python program to find the duplicate values of an array of string values.
# def duplicate(arr):
#     new = []
#     for i in range(len(arr)):
#         if arr[i] in arr[i+1:]:
#             new.append(arr[i])
#     return new
#
# print(duplicate(["hello","humpty","Dumpty","hello"]))


# 14. Write a python program to find the common elements between two arrays (string values).

# def common_elements(arr1,arr2):
#     common = []
#     for i in range(len(arr1)):
#         if arr1[i] in arr2:
#             if arr1[i] not in common:
#                 common.append(arr1[i])
#     return common
# print(common_elements([2,34,5,6,7,2,6,8],[1,2,3,4,5,6,7]))


# 15. Write a python program to find the common elements between two arrays of integers.
# 
# 
# 
# 16. Write a python program to remove duplicate elements from an array. 

# Python code to remove duplicate elements

# def Remove(duplicate):
#     final_list = []
#     for num in duplicate:
#         if num not in final_list:
#             final_list.append(num)
#     return final_list
#
# duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
# print(Remove(duplicate))

# 17. Write a python program to find the second largest element in an array.


# 18. Write a python program to find the second smallest element in an array.

# def second(arr):
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]> arr[j]:
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp
#     return arr[1]
# print(second([2,5,4,8,97,3,56]))


# 19. Write a python program to add two matrices of the same size.
# l = [[1,2],
#      [3,4]]
# l1 = [[1,2],
#       [3,4]]
# copy=[]
# for i in range(len(l)):
#     for j in range(len(l)):
#         copy.append(l[i][j]+l[i][j])
#
# print(copy)


# 20. Write a python program to convert an array to ArrayList.
# no need
# 
# 
# 21. Write a python program to convert an ArrayList to an array. 
# 
# no need
# 
# 22. Write a python program to find all pairs of elements in an array
# whose sum is equal to a specified number.

# arr = [2, 3, -5, 5, 2, 7, 8, 6, 16]
# f = 11
# for i in range(len(arr)):
#     for j in range(i + 1):
#         if arr[i] + arr[j] == f:
#             print(f"{arr[i]} + ({arr[j]}) = {f}")

# 23. Write a python program to test the equality of two arrays.

# def equality(arr1, arr2):
#     f = True
#     for i in range(len(arr1)):
#         for j in range(len(arr2)):
#             if arr1[i] != arr2[j]:
#                 f = False
#             else:
#                 f = True
#     return f
#
#
# print(equality([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))

# 24. Write a python program to find a missing number in an array.
# 
# 
# 
# 25. Write a python program to find common elements from three sorted
# (in non-decreasing order) arrays.
# 
# 
# 
# 26. Write a python program to move all 0's to the end of an array.
# Maintain the relative order of the other (non-zero) array elements.
# 
# 
# 
# 27. Write a python program to find the number of even and odd integers in a given array
# of integers.

# can be dne

# 28. Write a python program to get the difference between the largest and smallest
# values in an array of integers. The length of the array must be 1 and above.

# def largest_smallest(arr):
#     maxx = arr[0]
#     minn = arr[1]
#     for i in range(len(arr)):
#         if minn > arr[i]:
#             minn = arr[i]
#         else:
#             maxx = arr[i]
#     return maxx - minn
#
#
# print(largest_smallest([2, 4, 1, 3, 4, 5, 9, 88]))

# 29. Write a python program to compute the average value of an array of integers
# except the largest and smallest values.

# def largest_smallest(arr):
#     maxx = arr[0]
#     minn = arr[1]
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#
#
# print(largest_smallest([2, 4, 1, 3, 4, 5, 9, 88]))

# 30. Write a python program to check if an array of integers without 0 and -1.
# 
# can be done
# 
# 31. Write a python program to check if the sum of all the 10's in the array is exactly 30.
# Return false if the condition does not satisfy, otherwise true.

# def tens(arr):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] == 10:
#             count += 1
#     if count != 3:
#         print("False")
#     else:
#         print("True")
#
#
# tens([4, 5, 6, 10, 7, 10, 8, 10, 10])

# 32. Write a python program to check if an array of integers contains
# two specified elements 65 and 77.

# can be done


# 33. Write a python program to remove the duplicate elements of a given array and
# return the new length of the array.
# Sample array: [20, 20, 30, 40, 50, 50, 50]
# After removing the duplicate elements
# the program should return 4 as the new length of the array.

# def duplicates(arr):
#     new = []
#     for i in range(len(arr)):
#         if arr[i] not in new:
#             new.append(arr[i])
#
#     return len(new)
#
#
# print(duplicates([20, 20, 30, 40, 50, 50, 50]))

# 34. Write a python program to find the length of the longest consecutive elements
# sequence from a given unsorted array of integers.
# Sample array: [49, 1, 3, 200, 2, 4, 70, 5]
# The longest consecutive elements sequence is [1, 2, 3, 4, 5],
# therefore the program will return its length 5.


# 35. Write a python program to find the sum of the two elements of a given array
# which is equal to a given integer.
# Sample array: [1,2,4,5,6]
# Target value: 6.  
# 
# 
# 
# 36. Write a python program to find all the unique triplets such that sum of all the three elements [x, y,
# z (x ≤ y ≤ z)] equal to a specified number. Sample array: [1, -2, 0, 5, -1, -4] Target value: 2.
# 
# 
# 
# 37. Write a python program to create an array of its anti-diagonals from a given square matrix.  
# 
# Example:
# Input :
# 1 2
# 3 4
# Output:
# [
# [1],
# [2, 3],
# [4]
# ]

# l = [[1, 2],
#      [3, 4], [5, 6]]
#
#
# def anti_diagmnoal(l):
#     copy = []
#     for i in range(len(l)):
#         for j in range(i + 1):
#             copy.append([l[i][j:]])
#             copy.append([l[i][len(l) - j - 1]])
#     return copy
#
#
# print(anti_diagmnoal(l))

# 38. Write a python program to get the majority element from a given array of integers
# containing duplicates.
# Majority element: A majority element is an element
# that appears more than n/2 times where n is the size of the array.
# 
# 
# 
# 39. Write a python program to print all the LEADERS in the array.   
# Note: An element is leader if it is greater than all the elements to its right side.

# def leader(string):
#     d = []
#     for i in range(len(string)):
#         d.append(string[i])
#     return d
#
# print(leader("leader"))


# 40. Write a python program to find the two elements from a given array
# of positive and negative numbers such that their sum is closest to zero.


# def zero(arr):
#     pass

# 41. Write a python program to find smallest and second-smallest elements of a given array.

# def second(arr):
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]> arr[j]:
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp
#     return arr[0],arr[1]
# print(second([2,5,4,8,97,3,56]))


# 42. Write a python program to segregate all 0s on left side and
# all 1s on right side of a given array of 0s and 1s.
# 
# 
# 
# 43. Write a python program to find all combination of four elements of a given array
# whose sum is equal to a given value.
# 
# 
# 
# 44. Write a python program to count the number of possible triangles
# from a given unsorted array of positive integers.


# def possible_triangles(arr):
#     count = 0
#     for i in range(0, len(arr)):
#         for j in range(i + 1, len(arr)):
#             for k in range(i + 1, len(arr)):
#                 if (arr[i] + arr[j] > arr[k] & arr[i] + arr[k] > arr[j]
#                         & arr[k] + arr[j] > arr[i]):
#                     count += 1
#
#     return count
#
#
# print(possible_triangles([2, 3, 4, 5, 6, 7]))

# 45. Write a python program to cyclically rotate a given array clockwise by one.

# def cyclically(arr):
#     rotated = []
#     for i in range(len(arr)):
#         temp = arr[0]
#         for j in range(len(arr)):


# 46 Write a python program to check whether there is a pair
# with a specified sum of a given sorted and rotated array.

# 47. Write a python program to find the rotation count in a given rotated sorted array
# of integers.

# def rotated(arr):
#     min_value = arr[0]
#     min_index = -1
#     for i in range(1, len(arr)):
#         if min_value > arr[i]:
#             min_value = arr[i]
#             min_index = i
#     return min_index, arr
#
#
# print(rotated([35, 32, 30, 14, 18, 21, 27]))

# 48. Write a python program to arrange the elements of a given array of integers
# where all negative integers appear before all the positive integers.
# 
# done
# 
# 49. Write a python program to arrange the elements of a given array of integers
# where all positive integers appear before all the negative integers.


# can be done


# 50. Write a python program to sort an array of positive integers of a given array,
# in the sorted array the value of the first element should be maximum,
# second value should be minimum value, third should be second maximum,
# fourth second be second minimum and so on.

# def rearrange(arr, n):
#     # Auxiliary array to hold modified array
#     temp = n * [None]
#
#     # Indexes of smallest and largest elements
#     # from remaining array.
#     small, large = 0, n - 1
#
#     # To indicate whether we need to copy rmaining
#     # largest or remaining smallest at next position
#     flag = True
#
#     # Store result in temp[]
#     for i in range(n):
#         if flag is True:
#             temp[i] = arr[large]
#             large -= 1
#         else:
#             temp[i] = arr[small]
#             small += 1
#
#         flag = bool(1 - flag)
#
#     # Copy temp[] to arr[]
#     for i in range(n):
#         arr[i] = temp[i]
#     return arr
#
#
# # Driver program to test above function
# arr = [1, 2, 3, 4, 5, 6]
# n = len(arr)
# print("Original Array")
# print(arr)
# print("Modified Array")
# print(rearrange(arr, n))

# 51. Write a python program to separate 0s on left side
# and 1s on right side of an array of 0s and 1s in random order.

# def even_odd(a):
#     l = []
#     for i in range(len(a)):
#         if a[i] == 0:
#             l.append(a[i])
#     for i in range(len(a)):
#         if a[i] != 0:
#             l.append(a[i])
#     return l
#
#
# print(even_odd([1, 0, 1, 0, 1, 0, 0, 0, 1, 0]))

# 52. Write a python program to separate even and
# odd numbers of a given array of integers.
# Put all even numbers first, and then odd numbers.

# def even_odd(a):
#     l = []
#     for i in range(len(a)):
#         if a[i] % 2 == 0:
#             l.append(a[i])
#     for i in range(len(a)):
#         if a[i] % 2 != 0:
#             l.append(a[i])
#     return l
#
#
# print(even_odd([3, 6, 7, 4, 5, 6, 7, 0]))

# 53. Write a python program to replace every element with the next greatest
# element (from right side) in a given array of integers.

# def greatest(arr):
#     dup = []
#     for i in range(len(arr) - 1):
#         dup.append(max(arr[i + 1:]))
#     return dup
#
#
# print(greatest([45, 20, 100, 23, -5, 2, -6]))


# def sortt(arr):
#     for i in range(0, len(arr) - 1):
#         index = i
#         for j in range(i + 1, len(arr)):
#             if arr[index] > arr[j]:
#                 index = j
#         arr[i], arr[index] = arr[index], arr[i]
#     return arr
#
#
# print(sortt([4, 2, 6, 3, 9, 5, 3, 8, 6]))

# def sort(a):
#     for i in range(len(a) - 1):
#         for j in range(i + 1, len(a)):
#             if a[i] > a[j]:
#                 temp = a[i]
#                 a[i] = a[j]
#                 a[j] = temp
#
#     return a
#
#
# print(sort([8, 4, 6, 10, 6, 9]))

# Triplet problems
#
# limit = int(input("Enter upper limit:"))
# c = 0
# m = 2
# while c < limit:
#     for n in range(1, m + 1):
#         a = m * m - n * n
#         b = 2 * m * n
#         c = m * m + n * n
#         if c > limit:
#             break
#         if a == 0 or b == 0 or c == 0:
#             break
#         print(a, b, c)
#     m = m + 1
