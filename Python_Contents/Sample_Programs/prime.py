def prime(n):
	for i in range(2,n):
		if (n%i==0):
		   print(n ,"is not prime number")
		   break
	else:
			print(n," is prime number")



prime(7)
