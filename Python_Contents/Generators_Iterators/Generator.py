def simple_generator():
    yield "Bangalore"
    yield "Pune"
    yield "Mumbai"
    yield "Delhi"
    yield "Alahabad"


s = simple_generator()
# print(next(s))

# for i in s:
#     print(i)
# print(next((i)))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
