# binarySearch(arr, x, low, high)
#     if low > high
#         return False
#     else
#         mid = (low + high) / 2
#         if x == arr[mid]
#             return mid
#         else if x > arr[mid]        // x is on the right side
#             return binarySearch(arr, x, mid + 1, high)
#         else                               // x is on the left side
#             return binarySearch(arr, x, low, mid - 1)

# Binary Search in python

def binarySearch(array, x, low, high):
    if high >= low:

        mid = low + (high - low) // 2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid - 1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array) - 1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
