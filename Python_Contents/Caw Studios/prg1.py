# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

# Input: s = "abBAcC"
# Output: ""
# Explanation: We have many possible scenarios, and all lead to the same answer. For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""

# Input: s = "s"
# Output: "s"
# gg = "dd"
# gg.rep


def check_the_String(stringg, i):
    if len(stringg) == 0:
        return ""
    elif len(stringg) == 1:
        return stringg
    else:
        while i < len(stringg) - 1:
            if stringg[i].isupper() or stringg[i + 1].isupper():
                if len(stringg) == 0 or len(stringg) == 1:
                    return stringg
                stringg = stringg[:i] + stringg[i + 2:]
                check_the_String(stringg, 0)
            else:
                pass
            i = i + 1
        else:
            return stringg


print(check_the_String("leeEtCode", 0))
