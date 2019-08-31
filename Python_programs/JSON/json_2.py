import json
from decimal import Decimal

# json string
json_string  = '{"drink":["coffee","tea","cold drinks"]}'
#json_string = '{"eatable":["Dosa","Idli","Puri"]}'
print(json_string[0])
obj = json.loads(json_string)

for drink in obj['drink']:
    print(drink)


print(type(obj))

#for eat in obj['eatable']:
#   print(eat)

'''
jsondata = '{"number": 1.573937639}'
x = json.loads(jsondata, parse_float=Decimal)
#x = json.loads(jsondata)#, parse_float=Decimal)
print(x["number"])
print(type(x["number"]))
'''