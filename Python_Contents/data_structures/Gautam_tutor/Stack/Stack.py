class Stack:

    def __init__(self):
        self.data =[]
        while(True):
            temp_limit = input("Enter the limit of Stack = ")
            if( temp_limit.isdigit() ):
                self.limit = int( temp_limit )
                break
            else:
                print("Enter the integer length.")

    def push(self):
        if( len( self.data ) < self.limit ):
            self.data.append( input("Enter a data = ") )
            return "Data Inserted"

        else:
            return "Stack Over Flow"

    def pop(self):
        if( len( self.data ) > 0 ):
            return self.data.pop()

        else:
            return "Stack UnderFlow"

    def disp(self):
        return self.data

stack_list = []

while(True):
    print( "1. Create New Stack 2. See the number of Stacks, 3. Delete Stack,  4.Do Operation on Stack, 5.Exit" )
    op = input("Enter the option = ")

    if( op.isdigit() ):
        op = int( op )

        if(op == 1 ):
            stack_list.append( Stack() )
            print("Stack Created")

        elif( op == 2 ):
            print( f"There are { len(stack_list) } stacks" )

        elif( op == 3 ):
            if( len(stack_list) > 0 ):
                print("There are following elements in the stacks,")
                for i in range( len(stack_list) ):
                    print(f"Stack {i+1} = { stack_list[i].disp() }" )

                print()
                del_stack_op = input("Which Stack number you want to delete from 1..n ? = ")

                if( del_stack_op.isdigit() ):
                    del_stack_op = int( del_stack_op )

                    if( del_stack_op> 0 and del_stack_op <= len( stack_list ) ):
                        stack_list.pop( del_stack_op - 1 )
                        print(f"Stack { del_stack_op } Deleted")
                    else:
                        print("Wrong Selection, Try Again.")

                else:
                    print("Select Correct Integer Option")
            else:
                print("There is no Stack Available")

        elif( op == 4 ):
            selected_stack = input("Which Stack number you want to select from 1..n ? = ")

            if( selected_stack.isdigit() ):
                selected_stack = int( selected_stack )

                if (selected_stack > 0 and selected_stack <= len( stack_list )):

                    selected_stack = stack_list[ selected_stack -1 ]

                    while(True):
                        op = input("1.Push, 2. Pop, 3. Print, 4.Exit Stack")

                        if( op.isdigit() ):
                            op = int( op )
                            if( op == 1 ):
                                print( selected_stack.push() )

                            elif( op == 2 ):
                                print( f"Deleted Data = { selected_stack.pop() }" )

                            elif( op == 3 ):
                                print( f"Data = { selected_stack.disp() }" )

                            elif( op == 4 ):
                                break
                            else:
                                print("Wrong Selection, Try Again")

                        else:
                            print("Select Correct Option")
                else:
                    print(f"Wrong Selection, Try Again. Selection starts from 1 to { len(stack_list) }")
            else:
                print("Select Correct Integer Option")

        elif( op == 5 ):
            break

        else:
            print(f"Wrong Selection, Try Again.")

    else:
        print("Select Correct Integer Option")