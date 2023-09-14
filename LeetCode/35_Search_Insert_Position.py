# nums = [1, 3, 5, 6]
# target = int(input("Enter your number: "))

# for i in range(len(nums)):
#     if nums[i] == target:
#         print(i)
#     else:
#         nums.append(target)
#         print(nums)

# print(nums)


# nums = [1, 3, 5, 6]
# target = int(input("Enter your number: "))

# found = False  # A flag to check if the target is found in the list

# for i in range(len(nums)):
#     if nums[i] == target:
#         print(i)
#         found = True
#         break  # Exit the loop when the target is found

# if not found:
#     nums.append(target)
#     print(nums)

# print(nums)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            return sorted(nums).index(target)
