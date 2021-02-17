# Variable Length Argument


def sum_of_nat_no(*d):
    print(type(d))
    # Tuple is iterable object. So we are making use of loop
    sum = 0
    i = 0
    l = len(d)
    while True:
        if i < l:
            sum += d[i]
            i = i + 1
        else:
            break
    return sum


print(sum_of_nat_no(1))
print(sum_of_nat_no(1, 2))
print(sum_of_nat_no(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(sum_of_nat_no(100, 200, 300, 400, 500))
