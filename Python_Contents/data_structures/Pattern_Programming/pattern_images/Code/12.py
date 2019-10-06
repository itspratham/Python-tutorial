# #@#@#
# @#@#
# #@#
# @#
# #

i=1
while i<=5:
    h=5
    while i<=h:
        if i%2==0:
          if h%2==1:
              print("@",end=" ")
          else:
              print("#",end=" ")
        if i%2==1:
          if h%2==1:
              print("#",end=" ")
          else:
              print("@",end=" ")
        h = h - 1
    print()
    i = i + 1







i=1
h=5
j=0
while i<=7:
    a=1
    b=1
    while a<=i+h:
        print(" ",end="")
        a=a+1
    while b<=i+j:
        print("*",end="")
        b=b+1
    print()
    j = j + 1
    h = h - 2
    i = i + 1


