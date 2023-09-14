# nums = [3, 2, 2, 3]
# val = 3

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2


# value count
# n = len(nums)
# count = 0
# for i in range(n):
#     if nums[i] == val:
#         count += 1
# print(count)


# n = len(nums)

# while val in nums:
#     nums.remove(val)
# print(len(nums))

# count = 0
# new_list = []
# for i in nums:
#     if i != val:
#         new_list.append(i)
#     else:
#         count += 1
# print(count)
# print(len(new_list))


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         index = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[index] = nums[i]
#                 index += 1
#         return index


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         while val in nums:
#             nums.remove(val)


k = 0

for i in range(len(nums)):
    if nums[i] != val:
        nums[k] = nums[i]
        k += 1

print(k)
