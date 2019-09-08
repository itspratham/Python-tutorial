'''
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return int(fib(n-1)+fib(n-2))


print(fib(4))


'''
'''
def prime(n):
    for i in range(2,(n)):
        if n%i==0:
            print("it is not  a prime number")
    else:
        print("it is prime number")


prime(2)
'''
def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(0))

