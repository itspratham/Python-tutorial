# Variable Length Argument


def sum_of_nat_no(*kwargs, **args):
    """
    This fuction depicts the usage of *args and **kwargs
    :param args: *arags, **kwargs
    :param kwargs:
    :return: any value
    """
    print(type(args))
    print(type(kwargs))

    # Tuple is iterable object. So we are making use of loop
    sum = 0
    for no in kwargs:
        sum += no
    print(kwargs)
    print(args)

    for k,v in args.items():
        print("{}-dffdf{}".format(k,v))
    return sum


print(sum_of_nat_no(1,2,a=10,b=20,c=30))
print(sum_of_nat_no(1,2,3,4,5,6,7,8,9,10,a=10,b=20,c=30))
#print(sum_of_nat_no(100,200,300,400,500))

print(sum_of_nat_no.__doc__)