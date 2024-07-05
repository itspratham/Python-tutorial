def multiply(a, b):
    try:
        f = a * b
    except Exception as e:
        print(e, "hello")
        return e
    return f


if __name__ == "__main__":
    multiply(23, 34 / 0)
    print(multiply(-23, 34))
    print(multiply("a/", 4))
    multiply("a", "b")
