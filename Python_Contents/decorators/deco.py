def parent(z):
    print("Printing from the parent() function.")

    def first_child(a):
        return "Printing from the first_child() function."

    def second_child(b):
        return "Printing from the second_child() function."

    # print(first_child())
    # print(second_child())

    return first_child
# z="ff"
# a="ff"
# b = "ss"
parent(2)(4)

# def number_1(a):
#    def number_2(b):
#       return a*b
#    return number_2
# print(number_1(3)(2))
