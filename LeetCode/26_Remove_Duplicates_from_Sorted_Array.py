nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

duplicate = []

number = len(nums)

for i in range(number - 1):
    if nums[i] <= nums[i+1]:
        duplicate.append(i+1)
    # else:
    #     nums[i] == nums[i+1]
    #     duplicate.append("_")

count = len(duplicate)

print(duplicate)
print(count)

# common = set(nums)

# number = len(common)

# print(common)
# print(number)
