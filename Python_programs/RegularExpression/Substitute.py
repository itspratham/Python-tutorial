import re

phone = "2004-959-559 # This is Phone Number3"

num = re.sub(r'#.*$', "hello", phone)
print("Phone Num : ", num)


num = re.sub(r'\d$', "helo", phone)
print("Phone Num : ", num)