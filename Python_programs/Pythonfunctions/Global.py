# Global Variable :4

a = 10
def foo():
    global a
    print (a)
    a = a +10
    print(a)




print("Value of a is {}".format(a))
print("Calling the function foo ")
foo()
print("Value of a is {}".format(a))

