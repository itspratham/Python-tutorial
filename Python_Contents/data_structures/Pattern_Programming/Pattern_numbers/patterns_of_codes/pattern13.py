for i in range(6):
    for j in range(6):
       if i==0 or i==5 or j==0 or j==5:
          print(1,end=" ")
       else:
           print(" ", end=" ")
    print(" ")