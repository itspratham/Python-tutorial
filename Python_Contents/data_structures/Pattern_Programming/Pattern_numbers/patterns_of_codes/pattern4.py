'''
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
'''
n = 7
for i in range(1, 8) :
    l = 6
    j = i
    for k in range(i) :
        print(j, end=' ')
        j = l + j
        l = l -1
    print()
















