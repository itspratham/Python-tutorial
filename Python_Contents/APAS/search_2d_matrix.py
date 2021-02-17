def search_a_two_d(l, target):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][j] == target:
                return True
    return False


print(search_a_two_d([[1, 3, 4, 6], [12, 45, 65, 32], [54, 76, 32, 56], [44, 90, 92, 99]], 50))
