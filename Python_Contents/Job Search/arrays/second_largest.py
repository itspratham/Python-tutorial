# second-largest number in list
# brute-force

# function
def second_largest(list):
    maximum = 0
    second_max = 0
    n = len(list)
    for i in range(0, n):
        if list[i] > maximum:
            second_max = maximum
            maximum = list[i]
        else:
            if list[i] > second_max:
                second_max = list[i]

    return second_max


# input of list
li = []
n = int(input("Enter size of list "))
for i in range(0, n):
    e = int(input("Enter element of list "))
    li.append(e)

# smallest
print("second largest in ", li, "is")
print(second_largest(li))
