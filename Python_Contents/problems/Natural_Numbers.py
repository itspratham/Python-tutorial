#Write a C program to print all natural numbers from 1 to n

# def Natural(n):
#     for i in range(1,n+1):
#         print(i,end=" ")
#
#     print()
#
# Natural(40)


#Write a C program to print all natural numbers in reverse (from n to 1).

# def Natural_Reverse(n):
#     for i in range(n,0,-1):
#         print(i,end=" ")
#     print()
#
# Natural_Reverse(60)


#Write a C program to print all alphabets from a to z.
# def A_Z():
#     for i in range(65,91):
#         print(chr(i),end=" ")
#     print()
# A_Z()

#Write a C program to print all even numbers between 1 to 100.
# def even():
#     i=0
#     while i<=100:
#         if i%2==0:
#             print(i,end=" ")
#         i=i+1
# even()


#Write a C program to print all odd number between 1 to 100.
# def odd():
#     i=0
#     while i<=100:
#         if i%2==1:
#             print(i,end=" ")
#         i=i+1
# odd()

#Write a C program to find sum of all natural numbers between 1 to n.
# def natural(n):
#     sum=0
#     for i in range(n+1):
#         sum=i+sum
#     print(sum)
#
# natural(6)


#Write a C program to find sum of all even numbers between 1 to n.
# def even(n):
#     sum=0
#     for i in range(n+1):
#         if i%2==0:
#             sum=i+sum
#     print(sum)
#
# even(6)


#Write a C program to find sum of all odd numbers between 1 to n.
# def odd(n):
#     sum=0
#     for i in range(n+1):
#         if i%2==1:
#             sum=i+sum
#     print(sum)
#
# odd(6)


#Write a C program to print multiplication table of any number.
# def mul(n):
#     for i in range(1,11):
#         print("{} x {} = {}".format(n,i,n*i))
#
# mul(80)


#Write a C program to count number of digits in a number.
# n=805
# count=0
# while (n!=0):
#     count=count+1
#     n//=10
# print(count)

#Write a C program to find first and last digit of a number.

# n=805
# count=0
# last=n%10 #last digit of the number
#
# first=n
# while (first >= 10):
#     first=first//10
#
# print(last,first)


#Write a C program to calculate sum of digits of a first and last digit.
# n=805
# count=0
# last=n%10 #last digit of the number
#
# first=n
# while (first >= 10):
#     first=first//10
#
# print(last+first)

#Write a C program to sum first and last digits of a number.
# n=805
# count=0
# last=n%10 #last digit of the number
#
# first=n
# while (first >= 10):
#     first=first//10
#
# print(last+first)

#Prime number program
def prime(n):
    for i in range(1,n+1):
       if n%(i//2)==0:
         print("{} is a prime number".format(n))
         break
       else:
           print("{} is not a prime number".format(n))
           break

prime(7)
