"""
try:
    statemensts
    statemensts
    statemensts
except Exception1 :
    stements
except Exception2 :
    statements
except Exception3 :
    statements
else:
    statments
finally:
    statments
"""


try:
    denom = int(input("Enter a denominator"))
    number = 100
    print(number/denom)
except ZeroDivisionError as e:
    print("You cannot devide any number by 0")
# else:
#     print("No exceptions are occured")
finally:
    print("Execution completed")
