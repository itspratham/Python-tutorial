# # Spiral traversal on a Matrix
# def spiral_traversal(max_row, max_col, matrix):
#     k = 0
#     l = 0
#     max_col = max_col - 1
#     max_row = max_row - 1
#     while k <= max_row and l <= max_col:
#         for i in range(l, max_col + 1):
#             print(matrix[k][i], end="->")
#         k += 1
#         for i in range(k, max_row + 1):
#             print(matrix[i][max_col], end="->")
#         max_col -= 1
#         if k <= max_row:
#             for i in range(max_col, l - 1, -1):
#                 print(matrix[max_row][i], end="->")
#             max_row -= 1
#         if l <= max_col:
#             for i in range(max_row, k - 1, -1):
#                 print(matrix[i][l], end="->")
#             l = l + 1
#
#
# spiral_traversal(4, 4, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
#
#
# # Search an element in a matrix
# def search(matrix, target):
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if matrix[i][j] == target:
#                 return True
#     return False
#
#
# print(search([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 55))

# Find median in a row wise sorted matrix
# Find row with maximum no. of 1's
matrix = [[1, 5, 1, 0, 1], [1, 3, 4, 5, 6], [1, 1, 1, 1, 1]]
M = 3
N = 5
map_dict = dict()
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 1:
            pass


# Print elements in sorted order using row-column wise sorted matrix
# Maximum size rectangle
# Find a specific pair in matrix
# Rotate matrix by 90 degrees

# Python3 program to rotate a matrix by 90 degrees


# An Inplace function to rotate
# N x N matrix by 90 degrees in
# anti-clockwise direction
# def rotateMatrix(mat, N):
#     # Consider all squares one by one
#     for x in range(0, int(N / 2)):
#
#         # Consider elements in group
#         # of 4 in current square
#         for y in range(x, N - x - 1):
#             # store current cell in temp variable
#             temp = mat[x][y]
#
#             # move values from right to top
#             mat[x][y] = mat[y][N - 1 - x]
#
#             # move values from bottom to right
#             mat[y][N - 1 - x] = mat[N - 1 - x][N - 1 - y]
#
#             # move values from left to bottom
#             mat[N - 1 - x][N - 1 - y] = mat[N - 1 - y][x]
#
#             # assign temp to left
#             mat[N - 1 - y][x] = temp
#
#         # Function to print the matrix
#
#
# def displayMatrix(mat, N):
#     for i in range(0, N):
#
#         for j in range(0, N):
#             print(mat[i][j], end=' ')
#         print("")
#
#     # Driver Code
#
#
# # Test case 1
# mat = [[1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [9, 10, 11, 12],
#        [13, 14, 15, 16]]

# Test case 2
# mat = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]
#
# # Test case 3
# mat = [[1, 2],
#        [4, 5]]

# rotateMatrix(mat, 4)

# Print rotated matrix
# displayMatrix(mat, 4)

# Kth smallest element in a row-cpumn wise sorted matrix


# Common elements in all rows of a given matrix
# A Program to prints common element
# in all rows of matrix

# Specify number of rows and columns
M = 4
N = 5


# prints common element in all
# rows of matrix
def printCommonElements(mat):
    mp = dict()

    # initialize 1st row elements
    # with value 1
    for j in range(N):
        mp[mat[0][j]] = 1

    # traverse the matrix
    for i in range(1, M):
        for j in range(N):

            # If element is present in the
            # map and is not duplicated in
            # current row.
            if (mat[i][j] in mp.keys() and
                    mp[mat[i][j]] == i):

                # we increment count of the
                # element in map by 1
                mp[mat[i][j]] = i + 1

                # If this is last row
                if i == M - 1:
                    print(mat[i][j], end=" ")
                # Driver Code


mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]

printCommonElements(mat)

# This code is contributed
# by Mohit kumar 29
