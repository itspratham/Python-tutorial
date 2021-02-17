"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
Click me to see the sample solution
"""

n = int(input("Sample value of n is: "))
print(f"The value of n+nn+nnn = {n + (n * n) + (n * n * n)}")
