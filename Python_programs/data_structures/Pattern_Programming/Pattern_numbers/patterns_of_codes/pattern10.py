j = 0
count = 1
n = 5
for i in range(1, 6):
    for k in range(i):
        print(count, end=' ')
        count = count + 1
    temp = count
    count = count - 2
    for k in range(1, i):
        print(count, end=' ')
        count = count - 1
    count = temp
    print()
