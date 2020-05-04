'''
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
'''
'''
num=1
for i in range(0,5):
    for j in range(0,i+1):
        print(num,end=" ")
        num=num+1
    print()
'''
'''
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

for i in range(0,6):
    for j in range(i-1,5):
        print("*",end=" ")

    print()
or
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

'''

'''
for i in range(0,5):
	print("*",end="\n")
for j in range(0,5)  :
    print("*",end=" ")
'''

'''
import math
for i in range(0,5):
    for j in range(i,float(math.log(i,10))):
        print("*",end="\n")
    print()
'''
'''
result_str="";
for row in range(0,7):
    for column in range(0,7):
        if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):
            result_str=result_str+"* "
        else:
            result_str=result_str+"  "
    result_str=result_str+"\n"
print(result_str)
'''
'''
result=""
for row in range(6):
    for column in range(6):
        if(column==0 or row==0 or row==5 and ((column>0 and column<3)) or (column==2 and (row>2 and row<5 ) or row==3 and(column>=3 and column<6 ) or column==5 and(row>3 and column<6))  ):
            result=result+"*"
        else:
            result=result+" "
    result=result+"\n"
print(result)
'''
'''
for i in range(1,10):
    for j in range(i):
        print(" ")
    print()
'''
'''
n = int(input("Input a number: "))

# use for loop to iterate 10 times
for i in range(1,11):
   print(n,'x',i,'=',n*i)
'''
'''
input1=int(input("enter the number"))
if input1==1:
    print("10.5")
else:
    print(21+(input1-2)*4)
'''
'''
level = int(input('Please input nth level: '))

N = level*2 + 5
for x in range(level+1):
    d = ' '.join(str(11**x))
    print('{d:^{N}}'.format(N=N, d=d))
'''

'''
print("Fourth Number Pattern")
lastNumber = 9
for i in range(1, lastNumber):
    for j in range(-1+i, -1, -1):
        print(format(2**j, "4d"), end=' ')
    print("")
'''


# inc=1
# ch = 65
# for i in range(0,8):
#     for j in range(0,inc):
#         x = chr(ch)
#         if 91<=ch<=97:
#             continue
#         print(x, end=" ")
#         ch = ch + 1
#     inc = inc + 1
#     print()