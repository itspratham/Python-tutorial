#input 41245
#output
# /****
# /*
# /**
# /****
# /*****


integer= input("Enter the numbers without space")
intb= list(map(int,integer.strip()))
k=1
for i in range(len(intb)):
    j=1
    while j<=i:
        print("/",end=" ")
    print(" ")

