# dt = {"a":"apple", "b":"bear", "c":"cat", "d":"dog"}
#
# # Dictionary Method # clear : Cleas the entire dictionay print (dt) dt.clear() # Difference between dt.clear() and
# del dt is first one delete the element from the dictionay but del will delete the entire dict print (dt)
#

dt = {"a": "apple", "b": "bear", "c": "cat", "d": "dog"}

k = ["a", "b", "c", "d"]
w = dt.fromkeys(k, 10)
print(w)
print(dt)

