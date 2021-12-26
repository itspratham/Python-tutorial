# Write a Python program to create an array
# of 5 integers and display the array items.
# Access individual element through indexes.


# array_num = array('i', [1,3,5,7,9])
# for i in array_num:
#     print(i)
# print("Access first three items individually")
# print(array_num[0])
# print(array_num[1])
# print(array_num[2])

# Write a Python program to append a new item to the end of the array.
# array_num = array('i', [1,3,5,7,9])
# array_num.append(7)
# print(array_num)

# Write a Python program to reverse the order of the items in the array.
# array_num = array('i', [1,3,5,7,9])
# array_num.reverse()
# print(array_num)

# Write a Python program to get the length in bytes of one array item in the internal representation.
# array_num = array('i', [1,3,5,7,9])
# print(array_num.itemsize)

# Write a Python program to get the current memory address and the length in
# elements of the buffer used to hold an arrays
# contents and also find the size of the memory buffer in bytes.

# array_num = array('i', [1,3,5,7,9])
# print(array_num.buffer_info())
# print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))


# Find the largest number in the array
# def find_the_largest(arr):
#     maximum_no = arr[0]
#     second_max = arr[0]
#     for i in arr:
#         if i > maximum_no:
#             second_max = maximum_no
#             maximum_no = i
#         elif i > second_max and i != maximum_no:
#             second_max = i
#     return second_max
#
#
# print(find_the_largest([3, 4, 2, 6, 7, 0, 1, 9, 10, 11]))
