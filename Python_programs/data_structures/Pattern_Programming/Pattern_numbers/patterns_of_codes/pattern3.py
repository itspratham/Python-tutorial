count = 2

def checkprime( num ):
    flag = False        #False True means number is not prime

    for i in range(2,num) :
        if( num%i == 0 ):
            flag = True    #True means number is prime
            break

    return flag

n = 8
for i in range(1, n+1):
    k = 1
    while( k<i+1 ):
        if (checkprime(count) == True):
            k = k - 1

        else:
            print(count, end=' ')

        count = count + 1
        k = k + 1

    print()