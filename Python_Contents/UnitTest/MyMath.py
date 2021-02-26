def multiply(a, b):
    try:
        return a * b
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print(multiply(23, 34))
    print(multiply(-23, 34))
    print(multiply("a", 4))
    print(multiply("a", "b"))
