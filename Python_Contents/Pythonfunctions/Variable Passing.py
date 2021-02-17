# Function Arguments


def add(x, y):
    x = x * x
    y = y * y
    return x + y


sum = add(1, 2)
sum = add(y=2, x=3)
print(sum)


# sum = add(12)


# Default

def add(x, y=1, z=1):
    x = x * x
    y = y * y
    return x + y + z


sum = add(2, 4)
print(sum)
sum = add(12)
print(sum)
