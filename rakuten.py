# # write a palindrome program
#
#
# # def palindrome(string):
# #     for i in range(len(string)//2):
# #         if string[i] != string[~i]:
# #             return False
# #     return True
#
# # print(palindrome(""))
#
# # string = "aaaabbccde"
# #
# # def remove_duplicate(string):
# #     l = set(string)
# #     for i in l:
# #         print(i, end=" ")
# #
# # remove_duplicate(string)
#
#
# # table_name -- Class
# # id
# # class_name
#
# # student
# # id
# # stu_name
# # class_id
# # how many student are there in per class
#
# # select class_name, count(student.id) from student inner join class on
# # student.class_id = class.id group by student.id;
#
# str1 = "abcde"
# str2 = "bcde"
str1 = "AGGTAB"
str2 = "GXTXAYB"
#
#
# # def ff(str1, str2, i, j, k):
# #     if i == len(str1):
# #         return 0
# #     if j == len(str2):
# #         return 0
# #
# #     if str1[i] == str2[j]:
# #         return 1 + ff(str1, str2, i + 1, j + 1, k+str1[i])
# #     else:
# #         return max(ff(str1, str2, i + 1, j, k), ff(str1, str2, i, j + 1, k))
# #
# # print(ff(str1, str2, 0, 0, ""))
#
def ff(str1, str2, i, j, traversal):
    if i == len(str1):
        return traversal
    if j == len(str2):
        return traversal

    if str1[i] == str2[j]:
        traversal = str2[j] + traversal
        ff(str1, str2, i + 1, j + 1, traversal)
        return traversal
    else:
        return max(ff(str1, str2, i + 1, j, traversal), ff(str1, str2, i, j + 1, traversal))


print(''.join(list(reversed(ff(str1, str2, 0, 0, "")))))


# Write a function to find whether each letter in the input string has even count in the string, if each letter has even count, then return True, else return False.
# Input: "LRRBBGLGGG"
# Output: True


string = "LRRBBGLGGG"

# def a_func(string):
#     a_dict = {}
#     for i in range(len(string)):
#         if string[i] not in a_dict:
#             a_dict[string[i]] = 1
#         else:
#             a_dict[string[i]] = a_dict[string[i]] + 1
#     for key, value in a_dict.items():
#         if value % 2 != 0:
#             return False
#     return True
#
#
# print(a_func(string))


# b_json = {
#     {
#         "a": {
#             "b": {"d": "h", "e": "i"},
#             "c": {"f": "j", "g": "k"},
#         }
#     }
# }









