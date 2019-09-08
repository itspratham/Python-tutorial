# Local Variable :
a = 10
def foo(a):
    B = 20
    print (a)
    a = a +10
    print(a)
    print("THe value of  B {}".format(B))



print("Value of a is {}".format(a))
print("Calling the function foo ")
foo(a)
print("Value of a is {}".format(a))

