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



def Rotate():
    array= list(input("Enter the array elements: "))
    rotation_orientation= int(input("Choose the option 1: Left Rotation 2: Right Rotation 3: Display Array: "))
    position = int(input("Enter the position of the array you want to rotatate from: "))

    if rotation_orientation==1:
        print(LeftRotate(array,position))
    elif rotation_orientation ==2:
        print(RightRotate(array,position))
    elif rotation_orientation == 3:
        return array
    else:
        print("Enter the right option")


Rotate()



# # Complete the hourglassSum function below.
# def hourglassSum(arr):
#     for_first=0
#     for_second=1
#     for_third=0
#     listt=[]
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             d = arr[i][for_first:for_first+3]+\
#             arr[i][for_second] + arr[i][for_third:for_third+3]
#             listt.append(d)
#         for_first=for_first+1
#         for_second = for_second+1
#         for_third = for_third +1
#     x = min(listt)
#     return x
#
#
# if __name__ == '__main__':
#
#     arr = []
#
#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))
#
#     result = hourglassSum(arr)
#
#     print(result)