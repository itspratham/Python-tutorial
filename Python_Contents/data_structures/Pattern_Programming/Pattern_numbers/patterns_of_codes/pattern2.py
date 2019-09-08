#
# h=0
# f=5
# for i in range(5):              #0, 1, 2, 3, 4
#     for k in range(i+1):        #
#         print(k+f,end=" ")      #5, 4 5,
#
#     for k in range(5+h):
#          print(5,end=" ")
#
#     print(" ")
#     h = h-1
#     f = f-1


D = int(input())
pi = 22 / 7
chocolate = 0
for i in range(D):
    g = input().split(' ')
    r = int(g[0])
    x = int(g[1])
    if (((pi) * (r ** 2))) < (100 * x):
        chocolate = chocolate + 1

print(chocolate)