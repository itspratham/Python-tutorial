def check(func):
    def _wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except:
            pass
    return _wrapper

# def init(x, y):
#     pass

@check
def add(x, y):
    return x + y

print(add(2,3))


# @check
# def mult(x, y):
#     return x * y
#
# @check
# def divide(x, y):
#     print(x / y)
#
# @check
# def sub(x, y):
#     print(x - y)

#check(init)

'''
def my_decorator(function):
    print("Something is happening before the function is called.")
    function()
    print("Something is happening after the function is called.")
    return str

@my_decorator
def fun1():
    print("This is fun1")

@my_decorator
def fun2():
    print("This is fun2")

fun1()
fun2()
'''


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def func1():
#     print("Whee!")
#
# func1()



