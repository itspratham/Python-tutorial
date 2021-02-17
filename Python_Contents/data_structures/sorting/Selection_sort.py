# Selection Sorting
import time

sort = input("Enter the numbers: ").split()


def selection_sort(sort):
    timee = time.time()
    sorted_list = list(map(int, sort))
    for i in range(len(sorted_list)):
        min_index = i
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[min_index] > sorted_list[j]:
                min_index = j
        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]
    x = list(sorted_list)
    timees = time.time()
    print("the time is {}".format(timees - timee))
    print(sorted_list)


selection_sort(sort)
