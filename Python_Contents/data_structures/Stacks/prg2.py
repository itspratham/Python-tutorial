from sys import maxsize

def create_stack():
    stack=[]
    return stack

def push_into_the_stack(item,stack):
    x=stack.append(item)
    print(f"{item} pushed into the stack")
    return stack

def isempty(stack):
    return len(stack)==0

def pop_from_the_stack(stack):
    if isempty(stack):
        print(f"stack is empty")
        return (-maxsize-1)
    x=stack.pop()
    print(f"{x} removed from the stack")
    return x

x=create_stack()
push_into_the_stack(10,x)
push_into_the_stack(20,x)
push_into_the_stack(30,x)
pop_from_the_stack(x)
pop_from_the_stack(x)
pop_from_the_stack(x)
pop_from_the_stack(x)
pop_from_the_stack(x)
push_into_the_stack(40,x)
pop_from_the_stack(x)
