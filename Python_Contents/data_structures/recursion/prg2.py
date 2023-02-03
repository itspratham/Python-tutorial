# Replace every array element with the product of every other element
# without using a division operator

# Input: {1, 2, 3, 4, 5}
# Output: {120, 60, 40, 30, 24}
#
# Input: {5, 3, 4, 2, 6, 8}
# Output: {1152, 1920, 1440, 2880, 960, 720}

# def multiply(arr1, arr2):
#     sol = arr1 + arr2
#     mul = 1
#     for i in range(len(sol)):
#         mul = mul * sol[i]
#     return mul
#
#
# def a_func(arr):
#     a_list = []
#     for i in range(len(arr)):
#         num = multiply(arr[:i], arr[i + 1:])
#         a_list.append(num)
#     return a_list
#
#
# print(a_func([5, 3, 4, 2, 6, 8]))


# Find all distinct combinations of a given length – I
# Given an integer array, find all distinct combinations
# of a given length k.
# For
# example,
#
# Input: {2, 3, 4}, k = 2
# Output: {2, 3}, {2, 4}, {3, 4}
#
# Input: {1, 2, 1}, k = 2
# Output: {1, 2}, {1, 1}, {2, 1}

# Function to print all distinct combinations of length `k`
# def findCombinations(A, n, k, subarrays, out=()):
#     # invalid input
#     if len(A) == 0 or k > n:
#         return
#
#     # base case: combination size is `k`
#     if k == 0:
#         subarrays.add(out)
#         return
#
#     # start from the next index till the first index
#     for i in reversed(range(n)):
#         # add current element `A[i]` to the output and recur for next index
#         # `i-1` with one less element `k-1`
#         findCombinations(A, i, k - 1, subarrays, (A[i],) + out)
#
#
# def getDistinctCombinations(A, k):
#     subarrays = set()
#     findCombinations(A, len(A), k, subarrays)
#     return subarrays
#
#
# if __name__ == '__main__':
#     A = [1, 2, 3]
#     k = 2
#
#     # process elements from right to left
#     subarrays = getDistinctCombinations(A, k)
#     print(subarrays)


# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid + 1

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index:", str(result))
else:
    print("Element is not present in array")
