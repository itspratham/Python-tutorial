# def longest_substring(stringg):
#     funn_string = ""
#     i = 0
#     while i < len(stringg):
#         if stringg[i] not in funn_string:
#             funn_string = funn_string + stringg[i]
#         i = i + 1
#     return funn_string
#
#
# print(longest_substring("GEEKSFORGEEKS"))
# print(longest_substring("bbbbb"))
# print(longest_substring("pwwkew"))
from collections import defaultdict


def longest_substring(string):
    present_String = " "
    a_list = defaultdict(list)
    for i in range(len(string)):
        if string[i] not in present_String:
            present_String = present_String + string[i]
            a_list[len(present_String)].append(present_String)
        else:
            present_String = string[i]
    ff = max(a_list.keys())
    return ''.join(a_list[ff]).strip()


print(longest_substring("aFTHdyrgtrog"))
"""
# Python3 program to find and print longest
# substring without repeating characters.

# Function to find and print longest
# substring without repeating characters.
def findLongestSubstring(string):
    n = len(string)

    # starting point of current substring.
    st = 0

    # maximum length substring without
    # repeating characters.
    maxlen = 0

    # starting index of maximum
    # length substring.
    start = 0

    # Hash Map to store last occurrence
    # of each already visited character.
    pos = {string[0]: 0}

    # Last occurrence of first
    # character is index 0

    for i in range(1, n):

        # If this character is not present in hash,
        # then this is first occurrence of this
        # character, store this in hash.
        if string[i] not in pos:
            pos[string[i]] = i

        else:
            # If this character is present in hash then
            # this character has previous occurrence,
            # check if that occurrence is before or after
            # starting point of current substring.
            if pos[string[i]] >= st:

                # find length of current substring and
                # update maxlen and start accordingly.
                currlen = i - st
                if maxlen < currlen:
                    maxlen = currlen
                    start = st

                # Next substring will start after the last
                # occurrence of current character to avoid
                # its repetition.
                st = pos[string[i]] + 1

            # Update last occurrence of
            # current character.
            pos[string[i]] = i

        # Compare length of last substring with maxlen
    # and update maxlen and start accordingly.
    if maxlen < i - st:
        maxlen = i - st
        start = st

    # The required longest substring without
    # repeating characters is from string[start]
    # to string[start+maxlen-1].
    return string[start: start + maxlen]


# Driver Code
if __name__ == "__main__":
    string = "GEEKSFORGEEKS"
    print(findLongestSubstring(string))

"""
