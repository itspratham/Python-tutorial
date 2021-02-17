# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# def say_whee():
#     print("Whee!")
#
# say_whe = my_decorator(say_whee)
#
#
# say_whe()


# def employee(x):
#     print("employee name is radha")
#     x()
#     print("her age is 19")
#     return str
#
# @employee
# def employee1():
#     print("the salary is 20k")
#
# employee1()


# @employee
# def employee2():
#     print("the salary is 40k")
#
# employee2()


def func(afun):
    def wrapper(*args, **kwargs):
        afun()
        print(args, kwargs)

    return wrapper


@func
def bbb():
    print("inside bobby")


bbb()
