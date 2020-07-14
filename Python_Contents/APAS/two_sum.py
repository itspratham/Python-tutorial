def two_sum(a,target):
    for i in range(len(a)):
        if a[i] + a[i+1] == target:
            return [i,i+1]

print(two_sum([3,2,7,11,15],26))