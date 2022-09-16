def find_the_second_largest_no(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [3, 0, 0, 2, 0, 4]
print(find_the_second_largest_no(arr))
