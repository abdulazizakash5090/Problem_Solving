# Linear Search Algorithm

# LinearSearch(array, key)
# for each item in the array
#     if item == value
#       return its index

# Linear Search in Python

def linearSearch(array, n, x):
    # Going through array sequentially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if (result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
