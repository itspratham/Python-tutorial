def qsort(inlist):
    if not inlist:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater


print(qsort([5, 3, 3, 2, 2, 4, 6, 3]))
