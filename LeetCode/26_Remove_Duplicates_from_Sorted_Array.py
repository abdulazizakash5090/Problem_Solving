nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# duplicate = []

# number = len(nums)

# for i in range(number - 1):
#     if nums[i] <= nums[i+1]:
#         duplicate.append(i+1)
#     # else:
#     #     nums[i] == nums[i+1]
#     #     duplicate.append("_")

# count = len(duplicate)

# print(duplicate)
# print(count)

# common = set(nums)

# number = len(common)

# print(common)
# print(number)

# nums = [1, 1, 2]
# expectedNums = []

# k = removeDuplicates(nums)
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j


class Solution:
    def removeDuolicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


# Source
# https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
