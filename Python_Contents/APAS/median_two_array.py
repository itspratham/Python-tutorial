def median_of_two_sorted_array(a1,a2):
    final = sorted(a1+a2)
    if len(final)%2==1:
        return final[len(final)//2]
    else:
        d= final[(len(final)//2)-1] + final[(len(final)//2)]
        return d/2

print(median_of_two_sorted_array([1,2,90754,98],[3,4.7574,86]))
