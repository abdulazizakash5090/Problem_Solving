import sys

max_index = sys.maxsize
print(max_index)  # Output: 9223372036854775807 on a 64-bit system

# Using maxsize as an index
my_list = [1, 2, 3, 4, 5]
index = sys.maxsize - 1
value = my_list[index]
print(value)  # Output: 5
