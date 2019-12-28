'''

def parent():
    print("Printing from the parent() function.")

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    print(first_child())
    print(second_child())
'''



from decorator.Decorators_1 import my_decorator

@my_decorator
def fun1():
    print("hi")

fun1()