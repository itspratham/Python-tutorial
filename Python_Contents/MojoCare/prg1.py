# # nums = [2,7,11,15], target = 9
# # 2,7
#
#
# def func(num_list, target):
#     for i in range(len(num_list)):
#         for j in range(i + 1, len(num_list)):
#             if num_list[i] + num_list[j] == target:
#                 return num_list[i], num_list[j]
#     return "Could not find any"
#
#
# print(func([2, 7, 11, 15], 9))


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

    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all
    # elements 0 from count to end.
    print(count)
    while count < n:
        arr[count] = 0
        count += 1


# Driver code
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)

# This code is contributed by "Abhishek Sharma 44"

