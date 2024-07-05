# def a_decorator(func):
#     def inner(*args, **kwargs):
#         f = func(*args, **kwargs)
#         try:
#             d = sum(f)
#             return d
#         except:
#             raise Exception
#     return inner
#
#
# @a_decorator
# def my_func(a,b):
#     return a,b
#
# print(my_func("6",5))

x = 1
y = 2
x, y = y, x
print(x)
print(y)
