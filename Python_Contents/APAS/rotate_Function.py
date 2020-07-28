def rota(arr):
    arr1 = arr
    l = []
    for i in range(len(arr)):
        k = 0
        for j in range(len(arr1)):
            h = arr[j] *j
            k = k + h
        l.append(k)
        f = arr.pop()
        arr.insert(0,f)
    return max(l)

print(rota([4,3,2,6]))

