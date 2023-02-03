# Input: s = "leEeetcode" Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2,
# both will result "leEeetcode" to be reduced to "leetcode".

# Input: s = "abBAcC"
# Output: ""
# Explanation: We have many possible scenarios, and all lead to the same answer. For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""

# Input: s = "s"
# Output: "s"
# gg = "dd"
# gg.rep


def check_the_String(stringg):
    extra_string = ''
    count = 0
    while len(stringg)+1 > count:
        if ord(stringg[count]) == ord(stringg[count + 1]) - 26:
            pass
        else:
            extra_string = extra_string + stringg[count]

        count = count + 1
    return extra_string


print(check_the_String("leeEtCode"))
