"""
Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
s = input("Enter the comma-separated numbers:").split(',')
print(s)
x = tuple(s)
print(x)
