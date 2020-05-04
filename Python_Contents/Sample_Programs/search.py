# #Linear Search
#
# def LinearSearch(arr,item):
#     for i in range(len(arr)):
#         if arr[i] == item:
#             print(f"{item} is found at {i+1}")
#
#     return
#
# LinearSearch([3,2,6,2,2,5,4],4)

#Binary Search

# def BinarySearch(arr,item):
#     arr = sorted(arr)
#     low = 0
#     high = len(arr) - 1
#     while low<=high:
#         mid = (low+high)//2
#         if arr[mid] == item:
#             return mid+1
#
#         if arr[mid]>item:
#             high = mid -1
#         else:
#             low = mid + 1
#
# print(BinarySearch([3,2,4,6,3,2,1,4],1))