import pandas

excel_data_df = pandas.read_excel('/Users/pratham/Downloads/Chola SME Financial CAM - OF SREE MEENASHI INDUSTRIES 1 (1) (1).xlsx', sheet_name='Repayment Surrogate')

json_str = excel_data_df.to_json()

print('Excel Sheet to JSON:\n', json_str)
# 'BT Multiplier '


# dict_new= {}
# for i in range(len(key)):
#     dict_new[key[i]] = ""
# print(dict_new)
# import json
# ff = json.dumps(dict_new)
# print(ff)