arry = [1, 0, 0, 0, 4, 2, 0, 0, 1, 0, 9, 2, 0, 0, 0, 1, 0, 0]

# new_array1 = []
# new_array2 = []
# for i in range(len(arry)):
#     if arry[i] != 0:
#         new_array1.append(arry[i])
#     else:
#         new_array2.append(arry[i])
#
# print(new_array1 + new_array2)

count = 0
print(len(arry))
arry1 = []
count1 = 0
while count < len(arry):
    if arry[count] == 0:
        arry.append(arry[count])
        del arry[count]
    count = count + 1

print(arry)
