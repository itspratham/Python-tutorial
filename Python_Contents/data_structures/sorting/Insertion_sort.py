sort = input("Enter the numbers: ").split()
def insertion_sort(sort):
    sort= list(map(int, sort))
    flag =0
    for j in range(0,len(sort)-1):
        for i in range(0,len(sort)-j-1):
            if (sort[i]>sort[i+1]):
                sort[i], sort[i+1] = sort[i+1], sort[i]
                flag=1
        if flag ==0:
            print("vbrhf")
            break
    x= list(sort)
    return x

print(insertion_sort(sort))

