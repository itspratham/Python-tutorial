# Given an array of integers, return indices of the two numbers such
# that they add up to a specific target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# def twoSum(nums, target):
#     seen = {}
#     for i, value in enumerate(nums):  # 1
#         remaining = target - nums[i]  # 2
#         if remaining in seen:  # 3
#             return [seen[remaining], i]  # 4
#         else:
#             seen[value] = i  # 5
#
# print(twoSum([3,2,7,11,7,15],26)
#       )


def removeDuplicates(nums):
    l = []
    for i in nums:
        if i not in l:
            l.append(i)

    return l


print(removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
