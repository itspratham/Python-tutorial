def LeftRotate(array,position):
   for i in range(position):
       temp= array[0]
       for j in range(len(array)-1):
           array[j]=array[j+1]
       array[len(array)-1]=temp

   return array

def RightRotate(array,position):
    for i in range(0, position):
        # Stores the last element of array
        last = array[len(array) - 1]
        for j in range(len(array) - 1, -1, -1):
            # Shift element of array by one
            array[j] = array[j - 1]
            # Last element of the array will be added to the start of the array.
        array[0] = last

    return array



def Rotate_no_of_times(array,position,Rotate_no_of_times):
    rotation_type = int(input("Enter the rotation type 1:Left 2:Right "))
    if rotation_type==2:
        for i in range(Rotate_no_of_times):
            arr = print(RightRotate(array,position))
    elif rotation_type ==1:
        for i in range(Rotate_no_of_times):
            arr = print(LeftRotate(array,position))
    else:
        print("Enter the correct option")
    return arr

# Rotate_no_of_times([6,4,9,76,8],2,3)


#Find maximum value of Sum(i*arr[i]) with only rotations on given array allowed
# Input: arr[] = {1, 20, 2, 10}
# Output: 72
# We can 72 by rotating array twice.
# {2, 10, 1, 20}
# 20*3 + 1*2 + 10*1 + 2*0 = 72


def MaxSum(array):
    n=len(array)
    list1=[]
    for i in range(n):
        sum1= int(array[i])*i
        list1.append(sum1)
    return sum(list1)

def Rotate():
    array= input("Enter the array elements: ").split(' ')
    rotation_orientation= int(input("""Choose the option 1: Left Rotation 2: Right Rotation 3: Display Array
                  4: Find maximum value of Sum(i*arr[i]) with only rotations on given array allowed: """))
    position = int(input("Enter the position of the array you want to rotatate from: "))
    Rotate_no_of_time = int(input("Enter the number of times to be rotated: "))

    if rotation_orientation==1:
        print(LeftRotate(array,position))
    elif rotation_orientation ==2:
        print(RightRotate(array,position))
    elif rotation_orientation == 3:
        print( array)
    elif rotation_orientation == 4:
        #sum1 = Rotate_no_of_times(array,position,Rotate_no_of_times=Rotate_no_of_time)
        print(MaxSum(array))
    else:
        print("Enter the right option")


Rotate()


#Reverse algorithms for rotation of array
# Let the array be arr[] = [1, 2, 3, 4, 5, 6, 7], d =2 and n = 7
# A = [1, 2] and B = [3, 4, 5, 6, 7]
#
# Reverse A, we get ArB = [2, 1, 3, 4, 5, 6, 7]
# Reverse B, we get ArBr = [2, 1, 7, 6, 5, 4, 3]
# Reverse all, we get (ArBr)r = [3, 4, 5, 6, 7, 1, 2]


# def ReverseArray(array):
#     n = len(array)
#     outer=[]
#     for i in range(n):
#        outer.append(array[n-i-1])
#     return outer
#
# def ExecuteProgram(array,d,n):
#     array1 = array[0:d]
#     array2 = array[d:n+1]
#     reverse1 = ReverseArray(array1)
#     reverse2 = ReverseArray(array2)
#     reverse = ReverseArray(array=reverse1+reverse2)
#     return reverse
#
#
# #Given a sorted and rotated array, find if there is a pair with a given sum
# def pairInSortedRotated(array,x,n):
#     i=0
#     while i<n:
#         if array[i]+array[i+1]==x:
#             print("Found True")
#             break
#         i = i + 1
#     return True
#
# array = [1, 2, 3, 4, 5, 6, 7]
#
# y= ExecuteProgram(array, d=2, n=7)
#
# pairInSortedRotated(array=y,x=13,n=7)

