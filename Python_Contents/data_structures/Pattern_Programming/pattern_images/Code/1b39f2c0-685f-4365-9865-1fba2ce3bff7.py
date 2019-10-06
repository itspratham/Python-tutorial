#input 41245
#output
# /****
# /*
# /**
# /****
# /*****


integer= input("Enter the numbers without space: ")
intb= list(map(int,integer.strip()))
i=1
intc=0
while i<=len(intb):
    h = 1
    print("/",end=" ")
    while h<=intb[intc]:
        print("*",end=" ")
        h=h+1
    print("")
    intc= intc+1
    i=i+1


