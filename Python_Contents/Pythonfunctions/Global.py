# Global Variable :4

a = 10


def foo():
    global a
    print(a, "hello")
    a = a + 10
    print(a, "hello1")

print(a, "a")
print("Value of a is {}".format(a))
print("Calling the function foo ")
foo()
print("Value of a is {}".format(a))
