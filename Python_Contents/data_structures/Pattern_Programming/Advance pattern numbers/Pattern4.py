#
# def plusMinus(arr):
#     for i in arr:
#         if i > 0== True:
#             count = count + 1
#         elif i<0 == True:
#                 count1=count1+1
#         else:
#             count2=count2+1
#     print(   ((count)/n),((count1)/n),((count2)/n))
#
#
# if __name__ == '__main__':
#     n = int(input())
#
#     arr = list(map(int, input().rstrip().split()))
#     count = 0
#     count1 = 0
#     count2 = 0
#
#     plusMinus(arr)








f=int(input()).split(' ')
max_add=0
min_add=0
for i in range(len(f)):
    x=min(int(f[i]))
    y=max(int(f[i]))
    max_add=sum(int(f[i]))-x
    min_add=sum(int(f[i]))-y
print(min_add,max_add)
