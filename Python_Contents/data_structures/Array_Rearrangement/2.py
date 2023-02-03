# Write a program to reverse an array or string
# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}
#
# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}


def arrae(arr):
    l1 = []
    n = len(arr)
    # i=0
    # while i<n:
    #     l1.append(arr[n-i-1])
    #     n = n-1
    for i in range(n):
        l1.append(arr[-i-1])
    return l1


arr = [1, 4, 7, 8, 6, 4, 5, 6]
print(arrae(arr))
