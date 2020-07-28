# # # class Hello(object):
# # #
# # #     def __init__(self):
# # #         self.__a ="10"
# # #
# # #     def __str__(self):
# # #         return (str(self.__a))
# # #
# # #     def __dis(self):
# # #         print("Good Morning")
# # #         print(self.__a)
# # #
# # # h = Hello()
# # # print(h)
# # # #h.dis()
# # # #print(h.a)
# #
# #
# # class Person:
# #     def __init__(self):
# #         self.name = 'Manjula'
# #         self.__lastname = 'Dube'
# #
# #     def PrintName(self):
# #         return self.name + ' ' + self.__lastname
# #
# #
# # # Outside class
# # P = Person()
# # print(P.name)
# # print(P.PrintName())
# # print(P._Person__lastname)
# #
# #
# # # class SeeMee:
# # #     def youcanseeme(self):
# # #         return 'you can see me'
# # #
# # #     def __youcannotseeme(self):
# # #         return 'you cannot see me'
# #
# #
# # # Outside class
# # # Check = SeeMee()
# # # # print(Check.youcanseeme())
# # # #
# # # # print(Check.__youcannotseeme())
# # # print(Check._SeeMee__last)
# # # print(Check._SeeMee__youcannotseeme())
# #
# #
# # #!/usr/bin/env python
# # class Person:
# #     def Hello(self, name=None):
# #         if name is not None:
# #             print('Hello ' + name)
# #         else:
# #             print('Hello ')
# # # Create instance
# # obj = Person()
# # # Call the method
# # obj.Hello()
# # # Call the method with a parameter
# # obj.Hello('Edureka')
#
#
# def product(a, b):
#     p = a * b
#     print(p)
#
#
# # Second product method
# # Takes three argument and print their
# # product
# def product(a, b, c):
#     p = a * b * c
#     print(p)
#
#
# # Uncommenting the below line shows an error
# # product(4, 5)
#
# # This line will call the second product method
# product(4, 5)
