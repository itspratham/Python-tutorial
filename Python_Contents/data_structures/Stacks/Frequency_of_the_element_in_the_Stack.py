# Python3 implementation of the approach
# freqMap is to map element to its frequency


freqMap = {}


# setMap is to map frequency to the
# element list with this frequency
setMap = {}


# Variable which stores maximum frequency
# of the stack element


max_freq = 0


# Function to insert x in the stack
def push(x):
    global max_freq
    if x not in freqMap:
        freqMap[x] = 0

    print("Frequency MAp:", freqMap)
    # Frequency of x
    freq = freqMap[x] + 1

    # Mapping of x with its Frequency
    freqMap[x] = freq

    # Update max_freq Variable
    if freq > max_freq:
        max_freq = freq
    print(freq, "freq")

    # Map element to its frequency list
    # If given frequency list doesn't exist
    # make a new list of the required frequency
    if freq not in setMap:
        setMap[freq] = []

    setMap[freq].append(x)
    print(setMap)

# Function to remove maximum frequency element


def pop():
    global max_freq

    # Remove element from setMap
    # from maximum frequency list
    top = setMap[max_freq][-1]
    setMap[max_freq].pop()

    # Decrement the frequency
    # of the popped element
    freqMap[top] -= 1

    # If whole list is popped
    # then decrement the max_freq
    if len(setMap[max_freq]) == 0:
        max_freq -= 1

    return top


# Driver code
if __name__ == "__main__":
    # Push elements to the stack
    push(4)
    push(6)
    push(7)
    push(6)
    push(8)

    # Pop elements
    print(pop())
    print(pop())
    print(pop())

# This code is contributed by AnkitRai01
