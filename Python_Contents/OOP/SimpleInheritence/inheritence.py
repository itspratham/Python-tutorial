#
# class Human(object):
#     # Constructor
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Student(Human):
#
#     def __init__(self, name, age,total, avg):
#         super().__init__(name,age)
#         self.total =total
#         self.avg = avg
#
#     def display(self):
#         print("Name:{}".format(self.name))
#         print("Age:{}".format(self.age))
#         print("Total:{}".format(self.total))
#         print("Average:{}".format(self.avg))
#
#     def __del__(self,total):
#         self.total =total
#
# s = Student("Jhon", 23,500,56)
#
#
# s.display()
# print(s.total)
#
#
# class Calculator:
#     def __init__(self,total):
#         self.total = total
#     @classmethod
#     def addNumbers(self):
#         pass
#
# f = Calculator(87)
# f.addNumbers.total


arr= [7,1,2,4]
l=[]
n= len(arr)
i = 0

while i<n-1:
    j = 0
    if arr[i]>arr[j+1]:
        arr.remove(arr[i])
        n=n-1
    print(arr)
    while j<n:
        print(arr[j], arr[i])
        if (arr[j] - arr[i])>-1:
            l.append(arr[j] - arr[i])
        j = j+1
    i = i+1
print(l)
print(max(l))





