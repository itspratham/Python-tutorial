# Variable Length Argument


def sum_of_nat_no(e,*d):
    print(type(d))
    # Tuple is iterable object. So we are making use of loop
    sum = 0
    for no in d:
        sum += no
    return sum


print(sum_of_nat_no(1,4,5))
#print(sum_of_nat_no(1,2))
#print(sum_of_nat_no(1,2,3,4,5,6,7,8,9,10))
#print(sum_of_nat_no(100,200,300,400,500))