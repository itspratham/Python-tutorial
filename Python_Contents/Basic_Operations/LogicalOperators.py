# Logical Operators
# and, or , not

a = 10
b = 20
c = 15
d = 20

# And
print(a > 2 and b > 2)  # a>2 is true and b>2 is true; True and True = True
print(a > 2 and b > 100)  # a>2 is true and b>100 is false; True and false = False
print(a > 200 and b > 2)  # a>200 is false and b>2 is true; False and True = False
print(a > 200 and b > 100)  # a>2 is false and b>2 is false; False and False = False

print(a > 2 or b > 2)  # a>2 is true and b>2 is true; True or True = True
print(a > 2 or b > 100)  # a>2 is true and b>100 is false; True or false = True
print(a > 200 or b > 2)  # a>200 is false and b>2 is true; False or True = True
print(a > 200 or b > 100)  # a>2 is false and b>2 is false; False or False = False

# NOT()
print(not (a > 2))  # Not(True) =  False
print(not (a < 2))  # Not(True) =  True

"""
if condition:
    value /statement if pass
else:
    value / statement if faile
    
 """

if a > 200 and b > 2:
    print("'a' is greater than 200")
else:
    print("'a' is less than 200")
