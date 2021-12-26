def Simple_Merge(C):
    if len(C) > 1:
        mid = len(C) // 2
        A = C[:mid]
        B = C[mid:]
        m = len(A)
        n = len(B)
        Simple_Merge(A)
        Simple_Merge(B)
        i = j = k = 0
        while i < m and j < n:
            if A[i] < B[j]:
                C[k] = A[i]
                i = i + 1
                k = k + 1
            else:
                C[k] = B[j]
                j = j + 1
                k = k + 1

        while i < m:
            C[k] = A[i]
            i = i + 1
            k = k + 1
        while j < n:
            C[k] = B[j]
            j = j + 1
            k = k + 1

    return C


def Print_Arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")


arr = input("Enter the numbers: ").split()
arr = list(map(int, arr))

print(Simple_Merge(arr))
