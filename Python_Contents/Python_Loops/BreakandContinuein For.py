string = "Hello  Worlqd"

for ch in string:
    if ch == " ":       # Continues if space is encountered
        continue
    if ch == 'q':       #Breaks if 'ch' encounters the 'q'
        break
    print ch,
else:
    print ("Done with the loop")

