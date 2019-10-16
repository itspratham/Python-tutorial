def print_matrix(matt):
    for i in matt:
        print(i)

def matrixx(matrix,clockwise):
    mat=matrix
    if len(mat)<=1:
        return "Matrix is empty"
    while (True):
        if clockwise==1:
            top = 0
            left = 0
            bottom = len(mat) - 1
            right = len(mat) - 1
            #import ipdb;ipdb.set_trace()
            while left < right and top < bottom:

                # Store the first element of next row,
                # this element will replace first element of
                # current row
                prev = mat[top + 1][left]

                # Move elements of top row one step right
                for i in range(left, right + 1):
                    curr = mat[top][i]
                    mat[top][i] = prev
                    prev = curr

                top += 1

                #Move elements of rightmost column one step downwards
                for i in range(top, bottom + 1):
                    curr = mat[i][right]
                    mat[i][right] = prev
                    prev = curr

                right -= 1

                # Move elements of bottom row one step left
                for i in range(right, left - 1, -1):
                    curr = mat[bottom][i]
                    mat[bottom][i] = prev
                    prev = curr

                bottom -= 1

                # Move elements of leftmost column one step upwards
                for i in range(bottom, top - 1, -1):
                    curr = mat[i][left]
                    mat[i][left] = prev
                    prev = curr

                left += 1

            return mat

        elif clockwise==2:
            top = 0
            left = 0
            bottom = len(mat) - 1
            right = len(mat) - 1
            while left<right and top<bottom:
                prev = matrix[top][right-1]
                for i in range(top,bottom+1):
                    curr = matrix[i][left]
                    matrix[i][left] = prev
                    prev=curr
                left = left + 1

                for i in range(left,right+1):
                    curr = matrix[bottom][i]
                    matrix[bottom][i]=prev
                    prev = curr
                bottom = bottom - 1

                for i in range(bottom,top-1,-1):
                    curr = matrix[i][right]
                    matrix[i][right]= prev
                    prev =curr
                right = right -1

                for i in range(right,left-1,-1):
                    curr = matrix[top][i]
                    matrix[top][i] = prev
                    prev = curr
                top = top + 1

            return matrix

        else:
            try:
                matrixx(matrix,clockwise)
            except:
                break

m=3
print("Enter the matrix: ")
matrix = []

for _ in range(m):
    matrix.append(list(map(int, input().rstrip().split())))
while True:
        rotation = int(input("Enter the no of elements it has to be rotated by: "))
        clockwise = int(input("Enter the direction 1:Clockwise 2:Anti-Clockwise: "))
        i = 1
        while i <= rotation:
            matt=matrixx(matrix=matrix, clockwise=clockwise)
            i = i + 1
        print_matrix(matt)
