import random
def lottory():
    for i in range(6):
        yield random.randint(1,100)

    #yield random.randint(1, 15)

l = lottory()
for i in l:
    print(i)