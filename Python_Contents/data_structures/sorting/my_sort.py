sort = input("Enter the numbers").split()
sort = list(map(int, sort))
import time
def mysort(sort):
    timee = time.time()
    sort1 = []
    while len(sort)!=0:
      minimum = min(sort)
      sort1.append(minimum)
      sort.remove(minimum)
    timees = time.time()
    print("the time is {}".format(timees - timee))
    return sort1

print(mysort(sort))


sort = input("Enter the numbers").split()
sort = list(map(int, sort))

def mysort1(sort):
    
    return sort

print(mysort1(sort))
