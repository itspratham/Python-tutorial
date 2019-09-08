'''
Write a Python program to accept a filename from the user and print the extension of that.
Go to the editor
Sample filename : abc.java
Output : java
'''

s=input("Enter the filename from the user: ")
print(f"Sample filename: {s}")
x=s.split('.')
print("Output : "+x[1])