# Python program to print all permutations with
# duplicates allowed

def toString(List):
    return ''.join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]


# Driver program to test the above function
string = "ABCDEF"
n = len(string)
a = list(string)
permute(a, 0, n)

# def permute(s, answer):
#     if len(s) == 0:
#         # print(answer, end=" ")
#         return
#
#
#     for i in range(len(s)):
#         ch = s[i]
#         left_substr = s[0:i]
#         right_substr = s[i + 1:]
#         print("left string:", left_substr,"right string:", right_substr, "answer:",answer+ch)
#         rest = left_substr + right_substr
#         permute(rest, answer + ch)
#
#
# # Driver Code
# answer = ""
#
# s = input("Enter the string : ")
#
# print("All possible strings are : ")
# permute(s, answer)
#
# # This code is contributed by Harshit Srivastava
