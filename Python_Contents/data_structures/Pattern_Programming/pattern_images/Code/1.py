#        *
#       ***
#      *****
#     *******
#    *********
#   ***********


i = 1
while i <= 6:
    j = 5
    while j >= i:
        print(" ", end=" ")
        j = j - 1

    k = 1
    while k <=i:
        print("*", end=" ")
        k = k + 1
    print()
    i = i+1






# n=6
# g=6
# f=1
# for i in range(n):
#     for j in range(g):
#         print(" ",end=" ")
#     for k in range(f):
#         print("*",end= " ")
#     f=f+2
#     print()
#     g=g-1
