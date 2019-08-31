"""
if condition:
    if condition:
         if condition:
             statements
         else:
             statements
    else:
        statments
elif:
    statement
    if condition:
        statements
    else:
        statements
else:
    statement

"""

# Number is greater than 10 , number greater that 20, number is grater than 30
number = 21



if number  > 10:
    if number   > 20:
        if number > 30:
            print "Number is greater than 30"
        else:
            print ("Number is less than 30")
    else:
        print ("Number is less than 20")
else:
    print ("Number is less than 10")