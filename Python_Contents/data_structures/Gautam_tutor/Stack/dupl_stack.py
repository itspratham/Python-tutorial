class Stack:
    def __init__(self):
        self.list=[]
        self.limit=int(input("Enter the limit of the stack"))

    def push(self):
        if (len(self.list)< self.limit):
           x= input("Enter the element to be entered into the Stack")
           self.list.append(x)
           return f"{x} inserted into stack"
        else:
            return "Stack Overflow"

    def pop(self):
        if len(self.list)>0:
           return f"{self.list.pop()} is popped"
        else:
            return "Stack Underflow"

    def disp(self):
        return self.list

stack = Stack()

while (True):
    print("1:Push into the Stack 2:Pop from the Stack 3:Display 4:Exit")
    op = int(input("Enter the option"))
    if op==1:
        print(stack.push())
    elif op == 2:
        print(stack.pop())
    elif op==3:
        print(stack.disp())
    else:
        break
