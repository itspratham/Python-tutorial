# arry = [1, 0, 0, 0, 4, 2, 0, 0, 1, 0, 9, 2, 0, 0, 0, 1, 0, 0]
#
# # new_array1 = []
# # new_array2 = []
# # for i in range(len(arry)):
# #     if arry[i] != 0:
# #         new_array1.append(arry[i])
# #     else:
# #         new_array2.append(arry[i])
# #
# # print(new_array1 + new_array2)
#
# count = 0
# print(len(arry))
# arry1 = []
# count1 = 0
# while count < len(arry):
#     if arry[count] == 0:
#         arry.append(arry[count])
#         del arry[count]
#     count = count + 1
#
# print(arry)


# Python3 code to move all zeroes
# at the end of array

# Function which pushes all
# zeros to end of an array.
def pushZerosToEnd(arr, n):
    count = 0  # Count of non-zero elements

    # Traverse the array. If element
    # encountered is non-zero, then
    # replace the element at index
    # 'count' with this element
    for i in range(n):
        if arr[i] != 0:
            # here count is incremented
            arr[count] = arr[i]
            count += 1
    print(arr)
    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all
    # elements 0 from count to end.
    while count < n:
        arr[count] = 0
        count += 1


# Driver code
arr = [1, 9, 8, 0, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)

# This code is contributed by "Abhishek Sharma 44"
