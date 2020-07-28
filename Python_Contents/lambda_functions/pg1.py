# x = lambda a: a + 10
# print(x(5))
#
# x = lambda a, b: a * b
# print(x(5, 6))
#
# x = lambda a, b, c: a + b + c
# print(x(5, 6, 2))
#
#
# def myfunc(n):
#     return lambda a: a * n
#
#
# def myfunc(n):
#     return lambda a: a * n
#
#
# mydoubler = myfunc(2)
#
# print(mydoubler(11))


# Write a Python program to create a lambda function that
# adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x
# with argument y and print the result

# c = lambda x: x+15
# print(c(6))

# d = lambda x,y:x*y
# print(d(6,7))
#

#Write a Python program to create a function that takes one argument,
# and that argument will be multiplied with an unknown given number.

# def fun(n):
#      return lambda x:x*n
#
# x = fun(3)
# print(x(4))



# Write a Python program to sort a list of tuples using Lambda.
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# print("Original list of tuples:")
# print(subject_marks)
# subject_marks.sort(key = lambda x: x[1])
# print("\nSorting the List of Tuples:")
# print(subject_marks)


#Write a Python program to sort a list of dictionaries using Lambda.
# models = [{'make':'Nokia', 'model':216, 'color':'Black'},
#           {'make':'Mi Max', 'model':2, 'color':'Gold'},
#           {'make':'Samsung', 'model': 7, 'color':'Blue'}]
# print("Original list of dictionaries :")
# print(models)
# sorted_models = sorted(models, key = lambda x: x['model'])
# print("\nSorting the List of dictionaries :")
# print(sorted_models)


#Write a Python program to filter a list of integers using Lambda.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Original list of integers:")
# print(nums)
# print("\nEven numbers from the said list:")
# even_nums = list(filter(lambda x: x%2 == 0, nums))
# print(even_nums)
# print("\nOdd numbers from the said list:")
# odd_nums = list(filter(lambda x: x%2 != 0, nums))
# print(odd_nums)


#Write a Python program to square and cube every number in a given list of integers using Lambda.

# f = list(map(lambda x:(x**2,x**3),range(0,10)))
# print(f)

#Write a Python program to find if a given string starts with a given character using Lambda.
# starts_with = lambda x: True if x.startswith('P') else False
# print(starts_with("pen"))


#Write a Python program to extract year, month, date and time using Lambda.
# import datetime
# now = datetime.datetime.now()
# year = lambda x: x.year
# month = lambda x: x.month
# day = lambda x: x.day
# t = lambda x: x.time()
# print("year", year(now))
# print("Month", month(now))
# print("Day", day(now))
# print("time",t(now))

# Write a Python program to check whether a given string is number or not using Lambda.
# c = lambda x: False if type(x) is "int" else True
# print(c("123"))

#Write a Python program to create Fibonacci series upto n using Lambda.

# from functools import reduce
#
# fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
#                               range(n - 2), [0, 1])
# print(fib_series(8))