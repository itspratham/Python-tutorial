def reverst(input):
    x= input.split(" ")
    x=x[-1::-1]
    output = ' '.join(x)
    return output

if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print(reverst(input) )


