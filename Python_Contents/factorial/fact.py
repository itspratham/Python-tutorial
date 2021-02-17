def factorial(number):
    # Error handling
    if not isinstance(number, int):
        raise TypeError("Sorry {0} must be an integer.".format(number))
    if not number >= 0:
        raise ValueError("Sorry. 'number' must be zero or positive.")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)

    return inner_factorial(number)


# Call the outer function.
x = "the factorial is: " + str(factorial(4)) + " "

print(x)
