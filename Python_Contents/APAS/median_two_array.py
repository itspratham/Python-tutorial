# def median_of_two_sorted_array(a1,a2):
#     final = sorted(a1+a2)
#     if len(final)%2==1:
#         return final[len(final)//2]
#     else:
#         d= final[(len(final)//2)-1] + final[(len(final)//2)]
#         return d/2
#
# print(median_of_two_sorted_array([1,2,90754,98],[3,4.7574,86]))


# Input :  arr[] =  {2, 5, 8, 4, 6, 11}, sum = 13
# Output :
# 5 8
# 2 11
# 2 5 6
#
# Input : arr[] =  {1, 5, 8, 4, 6, 11}, sum = 9
# Output :
# 5 4
# 1 8

# def print_all_subsets(arr,target):
#     l = []
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             temp = arr[j]
#             if arr[i] + temp < target:
#                 l.append([arr[i],arr[j]])
#
#
# print_all_subsets([3,4,5,3])



# Return true if there exists a sublist of A[0..n] with given sum
def subsetSum(A, n, sum):

	# return true if sum becomes 0 (subset found)
	if sum == 0:
		return True

	# base case: no items left or sum becomes negative
	if n < 0 or sum < 0:
		return False

	# Case 1. include current item in the subset (A[n]) and recur
	# for remaining items (n - 1) with remaining sum (sum - A[n])
	include = subsetSum(A, n - 1, sum - A[n])

	# Case 2. exclude current item n from subset and recur for
	# remaining items (n - 1)
	exclude = subsetSum(A, n - 1, sum)

	# return true if we can get subset by including or excluding the
	# current item
	return include or exclude


# Subset Sum Problem
if __name__ == '__main__':

	# Input: set of items and a sum
	A = [7, 3, 2, 5, 8]
	sum = 14

	print("Yes" if subsetSum(A, len(A) - 1, sum) else "No")
