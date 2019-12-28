#uncomplete
#Rearrange an array such that arr[i] = i
# Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
# Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]
#
# Input : arr = {19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
#               11, 10, 9, 5, 13, 16, 2, 14, 17, 4}
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#          11, 12, 13, 14, 15, 16, 17, 18, 19]

def array_re(arr):
    l1=arr.copy()
    x=-1
    while len(arr) > 0:
        for i in range(len(arr)):
            if i in arr:
                l1[i] = i
                del arr[i]
            else:
                    l1[i] = -1
                    arr.clear()
    return l1


print(array_re([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]))