# nums = [2, 7, 11, 15]
# target = 9


# def get_target_indices(nums, target):

#     for i in range(len(nums)):
#         for j in range(1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return i, j


# print(get_target_indices(nums, target))


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numMap = {}
#         n = len(nums)

#         # Build the hash table
#         for i in range(n):
#             numMap[nums[i]] = i

#         # Find the complement
#         for i in range(n):
#             complement = target - nums[i]
#             if complement in numMap and numMap[complement] != i:
#                 return [i, numMap[complement]]

#         return []  # No solution found


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numMap = {}
#         n = len(nums)

#         for i in range(n):
#             complement = target - nums[i]
#             if complement in numMap:
#                 return [numMap[complement], i]
#             numMap[nums[i]] = i

#         return []  # No solution found


# class Solution(object):
#     def twoSum(self, nums, target):
#         seen = {}

#         for i in range(len(nums)):
#             diff = target - nums[i]
#             if diff in seen:
#                 return [seen[diff], i]
#             else:
#                 seen[nums[i]] = i


# def get_target_indices(nums, target):

#     for i in range(len(nums)):
#         for j in range(1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return i, j


# def target_indices(nums, target):
#     numMap = {}
#     n = len(nums)
#     for i in range(n):
#         complement = target - nums[i]
#         print(complement)
#         if complement in numMap:
#             return [numMap[complement], i]
#         numMap[nums[i]] = i

#     return []  # No solution found


# nums = [2, 7, 11, 15]
# target = 9
# ans = target_indices(nums, target)
# print(ans)


from typing import List


def isPairSum(A: List[int], N: int,  X: int) -> bool:

    i = 0

    j = N-1

    while i < j:
        if A[i] + A[j] == X:
            return i+1, j+1

        elif A[i] + A[j] < X:
            i += 1

        else:
            j -= 1

    return False


# Driver code
if __name__ == "__main__":
    # array declaration
    arr = [2, 3, 5, 8, 9, 10, 11]

    val = 17

    arrSize = len(arr)

    arr.sort()

    print(isPairSum(arr, arrSize, val))


def two_sum(arr, target):
    pointer_one = 0
    pointer_two = len(arr) - 1

    while pointer_one < pointer_two:
        sum = arr[pointer_one] + arr[pointer_two]

        if sum == target:
            return True
        elif sum < target:
            pointer_one += 1
        else:
            pointer_two -= 1

    return False


print(two_sum([1, 3, 4, 8, 9], 11))

# Source
# https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/
