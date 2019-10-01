#A B C D E F F E D C B A
#  A B C D E E D C B A
#    A B C D D C B A
#      A B C C B A
#        A B B A
#          A A


def pattern(n):
    k = 5
    g=5
    for i in range(n):
        for j in range(i):
            print(" ",end= " ")
            j=j-1
        alpha = 65
        for h in range(0,k):
            print(chr(alpha),end=" ")
            alpha=alpha+1
        k=k-1
        alpha1=65
        b=4
        for h in range(0,g):
            print(chr(alpha1+b),end=" ")
            b=b-1
        g=g-1
        print(" ")

pattern(6)
