Str = "this is string example....wow!!!"
Str = Str.encode('base64','strict')

print("Encoded String: " + Str)
print("Decoded String: " + Str.decode('base64','strict'))