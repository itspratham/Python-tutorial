s = "aabbbcdddabb"
op = "a2b3c1d3a1b2"

# def prg(s):
#     initial_str = s[0]
#     output_str = ""
#     for i in range(len(s)-1):
#         prev_string = initial_str
#         next_str = s[i+1]
#         if prev_string == next_str:
#             count = count +1
#         else:
#             output_str = output_str + str(count)
#     return output_str
# print(prg(s))

# def func(s):
#     initial = s[0]
#     output_dict = {}
#     for i in range(len(s)):
#
#         if s[i] not in output_dict.keys():
#             output_dict = output_dict + s[i]
#         elif s[i] in output_dict.keys():
#             ou


# input = "I#a@m$@a p#yt$h%on"
# output = "n#o@h$@t y#p$m%aI"
#
# def reveese(input):
#     output = ""
#     special_char = ["#","@","%","$"]
#     for i in range(len(input)-1,-1):
#         if input[i] not in special_char:
#             output[i] = output + input[i]
#         else:
#             output[i] = input + output
#     return output
#
# print(reveese(input))


# str = "I am a 'python' developer"
#
# index_capture = []
# for i in range(len(str)):
#     count= 0
#     if str[i] == "'":
#         count = count + 1
#         if count == 1:
#             index_capture.append(i)
#         if count == 2:
#             index_capture.append(i)
#             break
#
# print(index_capture)
# print(str[index_capture[0+1]:index_capture[1]])


list_comhension = [i for i in range(10)]

f = lambda x:x+3





