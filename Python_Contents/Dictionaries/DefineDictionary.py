"""
Dictionary : Collection key and value pair
 dictionary_name {
    Key : Value
    Key : Value
    Key : Value
    Key : Value
}
"""

# Define a dictionay
d = {}
dt = dict()

print(type(d))
print(type(dt))
print(d)

# Define the values

d = {"a": "apple", 'a': "ssd", "b": "bear", "c": "cat", "d": "dog"}
print(d)
print(d.items())
d["e"] = "Elephant"
d["e"] = "Ele"
d[1] = "One"
d[1.1] = "One.One"
t = (2,)
d[t] = "Tuple"
print(d.items())
print(d["a"])
print(id(d[1]))

for k, v in d.items():
    print("{}\t{}".format(k, v))

print(d.items())  # List of Tuples
print(d.keys())  # Give you the keys of dictionary in list

for k in d.keys():
    print(k, d[k])

d["e"] = "Elephant"

print(d)

lst_of_key = ["b", "d"]
for k in lst_of_key:
    print(d[k])

# Keys can string, int

int_dict = {1: 1, 2: 2, 3: 3}
print(int_dict)

# tupple can be a key
t_dict = {(1, 2): 1, 2: {'a': "a"}, 3: [12, 3, 45]}
print(t_dict)
print(t_dict[3], t_dict[2])

# Functions
print(d)
print(len(d))
print(len(int_dict))

print(type(d))
s = str(d)
print(s)
print(s[0:5])
print(type(s))
