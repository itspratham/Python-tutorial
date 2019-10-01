a = 10
print(type(a))
b=20.45
print(type(b))
st = "Hello Rajesh"
print(type(st))
d = 122312343432234324234
print(type(d))
print("Hello world")
print("The variable a="+str(a)+" b="+str(b)+" c="+str(st))
print("The variable a={}, b={}, st={},d={}".format(a,b,st,d))

# a,b,c,d =100
a=100
b=100
c=100
d=100

#In Python
a=b=c=d=100
print ("a={},b={},c={},d{}".format(a, b, c, d))

# One more way, packing and unpacking
a,b,c,d = 10,20,30,"Hello"
print ("a={},b={},c={},d={}".format(a,b,c,d))
