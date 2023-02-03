# Write a program in C to copy One string to another using recursion. Go to the editor
# Test Data :
# Input the string to copy : w3resource


# def a_recursion(string, copy_string, i, n):
#     if i > n:
#         return copy_string
#     return a_recursion(string, copy_string + string[i], i + 1, n)
#
#
# sss = "w3resource"
# print(a_recursion(sss, "", 0, len(sss) - 1))


# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
def palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


# palindrome("abbad")

def longest(s):
    a_list = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            if palindrome(s[i:j + 1]):
                a_list.append(s[i:j + 1])
    print(a_list)
    if a_list:
        return max(a_list)
    else:
        return s


print(longest("babad"))
















