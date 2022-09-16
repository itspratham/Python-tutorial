# Selection Sorting
import time

sort = [2 ,1, 5, 6, 8, 4]


def selection_sort(sort):
    timee = time.time()
    sorted_list = list(map(int, sort))
    for i in range(len(sorted_list)):
        min_index = i
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[min_index] > sorted_list[j]:
                min_index = j
        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]
    timees = time.time()
    print("the time is {}".format(timees - timee))
    print(sorted_list)
    return sorted_list

# selection_sort(sort)



def selection_sort_1(sort):
    for i in range(len(sort)):
        min_index = i
        for j in range(i+1, len(sort)):
            if sort[min_index] > sort[j]:
                min_index = j
        sort[i],sort[min_index] = sort[min_index], sort[i]
    print(sort)

selection_sort_1(sort)