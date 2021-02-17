def convert(s, numRows):
    if s is None:
        return s
    if numRows == 0:
        return s
    if numRows == 1:
        return s
    rstr = ""
    for i in range(numRows):
        if i == 0:
            rstr += s[::numRows + (numRows - 2)]
        elif i == numRows - 1:
            rstr += s[i::numRows + (numRows - 2)]
        else:
            spacea = 2 * (numRows - i)
            spaceb = 2 * i
            counter = 0
            j = i
            while j < len(s):
                rstr += s[j]
                if counter % 2 == 0:
                    j += spacea
                else:
                    j += spaceb
                counter += 1
    return rstr


class Solution(object):
    pass


c = Solution()
print(convert("fnvfkevnjnjn", 3))
