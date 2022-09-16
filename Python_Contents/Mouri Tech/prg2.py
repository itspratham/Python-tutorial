# Example inputs and expected outputs:-
#
# Example 1:
# Input: nums = [1,3,6,7], target = 2
# Output: 1
#
# Example 2:
# Input: nums = [1,3,5,6], target = 4
# Output: 2
#
# Example 3:
# Input: nums = [1,2,5,6], target = 9
# Output: 4

# Input: nums = [1,3,5,6], target = 5
# Output: 2

def index_(nums_list, target):
    for i in range(len(nums_list)):
        if nums_list[i] == target:
            return i
        elif nums_list[i] > target:
            return i
        else:
            pass
    return len(nums_list)


lst1 = [1,3,5,6]
print(index_(lst1, 5))
