def merge_sort(C):
    if len(C) > 1:
        mid = len(C) // 2
        A = C[:mid]
        B = C[mid:]
        m = len(A)
        n = len(B)
        merge_sort(A)
        merge_sort(B)
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


C = [23, 45, 2, 67, 43]
print(merge_sort(C))
