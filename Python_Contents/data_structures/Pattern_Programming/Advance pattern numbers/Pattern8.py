i = 0
j = 0
k = 1
l = 1
direction = 1
matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print("Matrix before snake=")
i = 0
while i < 10:  # this loop is used to print one line of matrix
    j = 0
    while j < 10:  # this loop is used to print one element
        print(matrix[i][j], end='', flush=True)
        print(" ", end='', flush=True)
        if matrix[i][j] < 100:
            print(" ", end='', flush=True)
        if matrix[i][j] < 10:
            print(" ", end='', flush=True)
        j = j + 1
    print("")
    i = i + 1
i = 1
j = 0
k = 0
while i <= 100:  # this loop is used to set pattern
    matrix[j][k] = i
    if direction == 1:
        if k + 1 < 10:
            if matrix[j][k + 1] == 0:
                k = k + 1  # if direction=1 and matrix[j][k+1]=0
            else:
                j = j + 1  # if direction=1 and matrix[j][k+1]!=0
                direction = 2
        else:
            j = j + 1  # if k+1 is not smaller than 10
            direction = 2

    elif direction == 2:
        if j + 1 < 10:
            if matrix[j + 1][k] == 0:
                j = j + 1  # if direction=2 and matrix[j+1][k]=0
            else:
                direction = 3
                k = k - 1  # if direction=2 and matrix[j+1][k]!=0
        else:
            direction = 3
            k = k - 1  # if j+1 is not smaller than 10
    elif direction == 3:
        if k - 1 >= 0:
            if matrix[j][k - 1] == 0:
                k = k - 1  # if direction=3 and matrix[j][k-1]=0
            else:
                direction = 4
                j = j - 1  # if direction=3 and matrix[j][k-1]!=0
        else:
            direction = 4
            j = j - 1  # if k-1 is not greater than -1
    elif direction == 4:
        if j - 1 >= 0:
            if matrix[j - 1][k] == 0:
                j = j - 1  # if direction=4 and matrix[j-1][k]=0
            else:
                k = k + 1  # if direction=4 and matrix[j-1][k]!=0
                direction = 1
        else:
            k = k + 1  # if j-1 is not greater than -1
            direction = 1
    i = i + 1
print("Matrix after snake=")

i = 0
while i < 10:  # this loop is used to print one line
    j = 0
    while j < 10:  # this loop is used to print one element
        print(matrix[i][j], end='', flush=True)
        print(" ", end='', flush=True)
        if matrix[i][j] < 100:
            print(" ", end='', flush=True)
        if matrix[i][j] < 10:
            print(" ", end='', flush=True)
        j = j + 1
    print("")
    i = i + 1