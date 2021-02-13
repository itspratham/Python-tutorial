class Stack:
    def __init__(self):
        self.list = []
        self.limit = int(input("Enter the limit of the stack: "))

    def push(self):
        if len(self.list) < self.limit:
            x = input("Enter the element to be entered into the Stack: ")
            self.list.append(x)
            return f"{x} inserted into stack"
        else:
            return "Stack Overflow"

    def pop(self):
        if len(self.list) > 0:
            return f"{self.list.pop()} is popped"
        else:
            return "Stack Underflow"

    def disp(self):
        return self.list

    def Search_Element_in_the_Stack(self):
        if len(self.list) == 0:
            return "Stack is empty, Cannot find the element"
        else:
            print(self.list)
            search_element = input("Enter the element to be searched: ")
            for i in range(len(self.list)):
                if search_element in self.list:
                    return f"Found the element at {i + 1}th position"
                else:
                    return "Couldn't find the element in the stack"

    def Delete_All_The_Elements_In_The_Stack(self):
        if len(self.list) == 0:
            return "Already Empty"
        else:
            self.list.clear()
            return "The stack is empty now"


stack = Stack()

while True:
    print(
        "1:Push into the Stack 2:Pop from the Stack 3:Display 4:Enter the element you want to search in the Stack "
        "5:Empty the stack 6:Exit")
    op = int(input("Enter the option: "))
    if op == 1:
        print(stack.push())
    elif op == 2:
        print(stack.pop())
    elif op == 3:
        print(stack.disp())
    elif op == 4:
        print(stack.Search_Element_in_the_Stack())
    elif op == 5:
        print(stack.Delete_All_The_Elements_In_The_Stack())
    else:
        break
