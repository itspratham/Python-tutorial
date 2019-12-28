search = [565,2314,6,621,24,5]
number = int(input("Enter the number: "))
def Sequential_Search(search,number):
    for i in range(len(search)):
        if search[i] == number:
            print("The number is found at {}".format(i+1))
    return

Sequential_Search(search,number)



