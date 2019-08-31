"""
Sequnece
Continous number, strings, objects having a common variable name
Its accessed by index- and index always starts from 0
"""
# Define the empty list
lst1 = []
lst2 = list()

print(type(lst1))
print(type(lst2))
print(lst1)
print (lst2)

lst3 = [12,34,56,67,89,45]
print (lst3)

print(lst3[2])
print(lst3[0])
print(lst3[:])
print(lst3[2:4])
print(lst3[2:])
print(lst3[:3])
print(lst3[len(lst3)-1])

# Reverse Indexing
print(lst3[-2:6])


# using while loop
idx = 0
while idx < len(lst3):
    print (lst3[idx])
    idx+=1

# Using for loop
for idx in range(0,len(lst3)):
    print (lst3[idx])

# Pythonic way of writing list with loop (because of iterator)
for num in lst3:
    print (num)
"""
lst4= iter(lst3)
print dir(lst3)     # Iterable Object
print dir(lst4)     # Iterator Object
print(lst4.next())
print(lst4.next())
print(lst4.next())
print(lst4.next())
print(lst4.next())
print(lst4.next())





"""