class Human:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def disply_human(self):
        print("Name is : {}".format(self.name))
        print("Age: {}".format(self.age))


#
# if __name__ == "__main__":
#     h = Human("Hello", 23)
#     h.disply_human()
