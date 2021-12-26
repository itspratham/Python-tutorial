# un-complete
# Rearrange an array such that arr[i] = i
# Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
# Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]
#
# Input : arr = {19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
#               11, 10, 9, 5, 13, 16, 2, 14, 17, 4}
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#          11, 12, 13, 14, 15, 16, 17, 18, 19]

def array_re(arr):
    n = len(arr)
    l = [-1] * n
    for i in range(n):
        if -1 in arr:
            arr.remove(-1)
    for i in range(len(arr)):
        l[arr[i]] = arr[i]
    print(l)


array_re([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1])
array_re([19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4])
