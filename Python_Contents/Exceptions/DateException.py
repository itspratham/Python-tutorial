class DateException(Exception):
    def __init__(self, value):
        # print("Initialization method called")
        self.value = value

    def __str__(self):
        # print("__str__ called")
        return repr(self.value)


if __name__ == "__main__":
    e = DateException("Error")
    print(e)
