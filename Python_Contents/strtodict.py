# from collections import defaultdict
#
# d1 = [{'Pan_number': 'BNPPA', 'Name': 'ADIND', 'DOB': '21/10/1992', 'father_name': 'DINESH KUMAR SINGH'},
#       {'Pan_number': 'BNPPA2539D', 'Name': 'ADITYA ANAND', 'DOB': '21/10/1992', 'father_name': 'DINESH KUMAR SINGH'},
#       {'Pan_number': '', 'Name': 'ANJANA KUMARI', 'DOB': '1208/978', 'father_name': 'KRISHAN KEWAL MUNJAL'}]
# d2 = [{'testcase_no': 'TC1', 'test_scenario': 'All the parameters passed correctly', 'req_type': 'pan',
#        'expected_req_type': 'pan', 'Pan_number': ' ', 'Name': 'ADITYA ANAND', 'DOB': '21/10/1992',
#        'father_name': 'DINESH KUMAR SINGH'},
#       {'testcase_no': 'TC2', 'test_scenario': 'All the parameters passed correctly', 'req_type': 'pan',
#        'expected_req_type': 'pan', 'Pan_number': ' ', 'Name': 'ADITYA ANAND', 'DOB': '21/10/1992',
#        'father_name': 'DINESH KUMAR SINGH'},
#       {'testcase_no': 'TC3', 'test_scenario': 'All the parameters passed correctly', 'req_type': 'pan',
#        'expected_req_type': 'pan', 'Pan_number': 'BNPPA2539D', 'Name': 'ADITYA ANAND', 'DOB': '21/10/1992',
#        'father_name': 'DINESH KUMAR SINGH'}]
#
#
# test_remarks = defaultdict(list)
# for i in range(0, len(d1)):
#     k1 = set(d1[i].keys())
#     k2 = set(d2[i].keys())
#     common_keys = set(k1).intersection(set(k2))
#     for key in common_keys:
#         if d1[i][key] != d2[i][key]:
#             test_remarks['list%s' % i].append(
#                 d2[i]['testcase_no'] + key + ":" + str(d2[i][key]) + "  not matched " + str(d1[i][key]))
# print(test_remarks)


#
# Objective - your
# python
# program
# should
# print
# the
# recurring
# words and their
# count in the
# given
# string.
#
# Condition - No
# Dictionary, No
# Collection, No
# Set, No
# lambda , No Regular
# Expression, No
# specialized
# libraries

String = "Hello World Hello World I am a programmer"
String = String.split(' ')
# print(String)
dictt = {}

# for i in range(len(String)):
#     if String[i] not in dictt:
#         dictt[String[i]] = 1
#     else:
#         dictt[String[i]] = dictt[String[i]] + 1
#
# print(dictt)

listt = []
count_list = []
# print(len(String)
for i in range(len(String)):
    count = 1
    if String[i] not in listt:
        for j in range(i + 1, len(String)):
            if String[i] == String[j]:
                count = count + 1
        if count>1:
            listt.append(String[i])
            count_list.append(count)
f_ = []
for i in range(len(listt)):
    f_.append((listt[i], count_list[i]))

print(f_)

