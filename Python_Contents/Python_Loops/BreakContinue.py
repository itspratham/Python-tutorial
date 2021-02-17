# User gives input "quit" "Continue" , "Inbvalid Option"
user_input = True
while user_input:
    user_input = str(input("Enter the valid input:"))
    if user_input == "quit":
        print("You have entered break")
        break

    if user_input == "continue":
        print("You habe entered continue")
        continue

    print("Invalid input. Enter again")
    print("Hello World")
    print("Bye")
else:
    print("Stoping the loop")
