dt = {"a":"apple", "b":"bear", "c":"cat", "d":"dog"}

# Dictionary Method
# clear : Cleas the entire dictionay
print (dt)
dt.clear()
# Difference between dt.clear() and del dt is first one delete the element from the dictionay but del will delete the entire dict
print (dt)

# Copy
dt = {"a":"apple", "b":"bear", "c":"cat", "d":"dog"}
dt1 = dt.copy()
dt["e"] = "Elephant"
print(dt)
print(dt1)

print(id(dt))
print(id(dt1))

#### fromkeys
k = ["a","b","c","d"]
w = dt.fromkeys(k,10)
print(w)

# has_key present in Python 2.x but not in 3.x
#print(dt.has_key("z"))

# Get
print(dt.get("a","No value for the key"))
print(dt.get("Z","No value for the key"))
print(dt.get("u"))



print(dt)

print("d" in dt.keys())
print("Z" in dt.keys())

