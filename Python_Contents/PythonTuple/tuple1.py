# Tuple are sequence
# How to define tuple

t = ()
print(t)
print(type(t))

t1 = tuple()
print(t1)
print(type(t1))

t3 = (12, 3, 45, 66, 788, 553)
print(t3)

# Indexing and Reverse Indexing
print(t3[5])
print(t3[2:5])
print(t3[-1])

i = 0
while i < len(t3):
    print(t3[i])
    i = i + 1

# Automatically does iteration
for ele in t3:
    print(ele)


l = [21, 12, 121, 34]
t = (12, 12.34, "Hello", l)
print(t)

# Opeations in Tupple
t1 = (212, 334, 34345, 534)
t2 = (1, 2, 3, 4, 5, 6)

t3 = t1 + t2
print(t1)
print(t2)
print(t3)

# *
t1 = "Hello"
print((t1 + " ") * 10)

t1 = (212, 334, 34345, 534)
if 212 in t1:
    print("212 present")
else:
    print("212 not present")

# max, min, len

print(len(t1))
print(max(t1))
print(min(t1))
