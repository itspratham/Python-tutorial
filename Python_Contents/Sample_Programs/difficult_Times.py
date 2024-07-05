# Find a peak element which is not smaller than its neighbours

# def print_theno(array):
#     count = 1
#     a_list = []
#     last_count = len(array) - 1
#     while count < last_count:
#         flag = False
#         if array[count] > array[count - 1]:
#             flag = True
#         if flag:
#             if array[count + 1] < array[count]:
#                 flag = "Truee"
#         if flag == "Truee":
#             a_list.append(array[count])
#         count = count + 1
#     return a_list
#
#
# print(print_theno([10, 20, 15, 27, 23, 90, 67]))


# How do you find the largest and smallest number in an unsorted integer array? (solution)

# def find_(arr):
#     largest = 0
#     smallest = arr[0]
#     for i in range(len(arr)):
#         if arr[i] > largest:
#             largest = arr[i]
#         if smallest > arr[i]:
#             smallest = arr[i]
#     return largest, smallest
#
# print(find_([5,2,7,4,6]))


# def max_sum(arr):
#     max_so_far = -34324322424 - 1
#     max_ending_here = 0
#     s = 0
#     for i in range(len(arr)):
#         max_ending_here = max_ending_here + arr[i]
#         if max_ending_here > max_so_far:
#             max_so_far = max_ending_here
#             start = s
#             end = i
#         if max_ending_here < 0:
#             max_ending_here = 0
#             s = i+1
#     return max_so_far, arr[start:end+1]
#
#
# print(max_sum([-2, -3, 4, -1, -2, 1, 5, -3]))

# Program for array left rotation by d positions.

# def rotate(arr, d):
#     return arr[d:] + arr[:d]
#
#
# print(rotate([1,2,3,45,5], 3))
# How do you perform a binary search in a given array?

# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid + 1
#         elif arr[mid] > target:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return
#
#
# print(binary_search([1, 2, 3, 4, 5], 3))


# Python3 program to demonstrate auto-complete
# feature using Trie data structure.
# Note: This is a basic implementation of Trie
# and not the most optimized one.


class TrieNode():
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False


class Trie():
    def __init__(self):

        # Initialising the trie structure.
        self.root = TrieNode()

    def formTrie(self, keys):

        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for key in keys:
            self.insert(key)  # inserting one key to the trie.

    def insert(self, key):

        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.
        node = self.root

        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]
        node.last = True

    def suggestionsRec(self, node, word):

        # Method to recursively traverse the trie
        # and return a whole word.
        if node.last:
            print(word)

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def printAutoSuggestions(self, key):

        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.
        node = self.root

        for a in key:
            # no string in the Trie has this prefix
            if not node.children.get(a):
                return 0
            node = node.children[a]

        # If prefix is present as a word, but
        # there is no subtree below the last
        # matching node.
        if not node.children:
            return -1

        self.suggestionsRec(node, key)
        return 1


# Driver Code
keys = ["hello", "dog", "hell", "cat", "a",
        "hel", "help", "helps", "helping"]  # keys to form the trie structure.
key = "h"  # key for autocomplete suggestions.

# creating trie object
t = Trie()

# creating the trie structure with the
# given set of strings.
t.formTrie(keys)

# autocompleting the given key using
# our trie structure.
comp = t.printAutoSuggestions(key)
if comp == -1:
    print("No other strings found with this prefix\n")
elif comp == 0:
    print("No string found with this prefix\n")

# This code is contributed by amurdia and muhammedrijnas
