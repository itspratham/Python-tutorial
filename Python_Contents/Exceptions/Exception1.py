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
    l=[00]
    print(l[0])
    raise IndexError
except ZeroDivisionError as e:
    print("You cannot devide any number by 0")
except IndexError as e:
    print("Index out of range")
except EOFError as e:
    print("Somebody pressed control d")
except Exception as e:
    print(e)


else:
    print("No exceptions are occured")
finally:
    print("Execution completed")
