import random


def lottory():
    for _ in range(6):
        yield _

    # yield random.randint(1, 15)


l = lottory()
print(next(l))
print(next(l))
print(next(l))
