def longest_substring(stringg):
    funn_string =""
    i=0
    while i<len(stringg):
        if stringg[i] not in funn_string:
            funn_string = funn_string + stringg[i]
        i = i+1
    return funn_string

print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))
