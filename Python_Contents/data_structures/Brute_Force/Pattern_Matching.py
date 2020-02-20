String = "fun-uncle"
Sub_String ="unc"
def Pattern_Matching(String,Sub_String):
    n= len(String)
    m = len(Sub_String)
    for  i in range(0 ,n-m+1):
        j=0
        while j<m and Sub_String[j] == String[i+j]:
            j = j+1
        if j == m :
            print("Substring is found at {}".format(i + 1))
            return i
    #print("Substring is found at {}".format(i+1))
Pattern_Matching(String,Sub_String)
