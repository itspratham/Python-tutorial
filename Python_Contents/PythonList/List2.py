# Replacing a index value in list
l = [23,45,8]
lst = [12,3,4556,6,7,88,l]
print(lst)
lst[1] = 1004
print(lst)

def foo():
    print("Im function")

# You can put any datatype in list
lst1 = [12,23.45,"Hello",lst,foo]
print(lst1[3][6][1])
lst1[4]()


### List Functions
print(len(lst))
print(len(l))
print(len(lst1))
print(l)
print(max(l))
print(min(l))


# List Operations
l1 = [123,432,456]
l2 = [6767,676,6667]
l3 = l1 + l2
print (l1)
print (l2)
print (l3)

print(123 in l1)
print(123 in l2)
print(l1*4)


# Methods
# append
print(l1)
l1.append(11)
print(l1)
# Insert
l1.insert(2,100)
print(l1)

# pop
print(l1.pop())
print(l1)
print(l1.pop())
print(l1)
print(l1.pop())
print(l1)



print(l1)
print(l2)
l1.extend(l2)

l1.remove(123)
print(l1)

l1.remove(l2[2])
print(l1)

print("=======================")
l3 = [772,232,545,5656,-89]
l3.reverse()
print(l3)

l3.sort()
l3.reverse()
print(l3)