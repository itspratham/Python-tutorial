# Membership Operator
# in  and not in

st = "ABCDEFGH1H0"
st1 = "SDJKEJNDNYEBWTUSNFKLGLJER"
# String is a Sequence
for char in st:
    print(char)

# in
c = "E" in st
print(c)

c = "X" in st
print(c)

# Not in
c = "E" not in st
print(c)

c = "X" not in st
print(c)

c = "10" in st
print(c)

c = "01" in st
print(c)

c = "1" in st and '0' in st
print(c)
