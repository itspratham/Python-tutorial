String = "fun-uncle"
Sub_String = "unc"


def Pattern_Matching(String, Sub_String):
    n = len(String)
    m = len(Sub_String)
    print(n-m+1)
    for i in range(0, n - m + 1):
        j = 0
        while j < m and Sub_String[j] == String[i + j]:
            j = j + 1
        if j == m:
            print("Substring is found at {}".format(i + 1))
            return i + 1
    # print("Substring is found at {}".format(i+1))


Pattern_Matching(String, Sub_String)
