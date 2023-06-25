# def linearSearch(array, n, x):

#     for i in range(0, n):
#         if (array[i] == x):
#             return i
#     return -1


# array = [2, 4, 0, 1, 9]
# x = 1
# n = len(array)
# result = linearSearch(array, n, x)
# if (result == -1):
#     print("Element not found")
# else:
#     print("Element found at index ", result)


# def binarySearch(array, x, low, high):

#     while low <= high:

#         mid = low + (high - low) // 2

#         if array[mid] == x:
#             return mid

#         elif array[mid] < x:
#             low = mid + 1

#         else:
#             high = mid - 1
#     return -1


# array = [3, 4, 5, 6, 7, 8, 9]
# x = 4

# result = binarySearch(array, x, 0, len(array)-1)

# if result != -1:
#     print("Element is present at index " + str(result))
# else:
#     print("Not found")


# def binarySearch(array, x, low, high):

#     if high >= low:

#         mid = low + (high - low)//2

#         if array[mid] == x:
#             return mid

#         elif array[mid] > x:
#             return binarySearch(array, x, low, mid-1)

#         else:
#             return binarySearch(array, x, mid+1, high)
#     else:
#         return -1


# array = [3, 4, 5, 6, 7, 8, 9]
# x = 5

# result = binarySearch(array, x, 0, len(array)-1)

# if result != -1:
#     print("Element is present at index " + str(result))
# else:
#     print("Not found")


# import sys


# def slectionSort(array, size):

#     for step in range(size):
#         min_idx = step

#         for i in range(step + 1, size):

#             if array[i] < array[min_idx]:
#                 min_idx = i

#         (array[step], array[min_idx]) = (array[min_idx], array[step])


# data = [-2, 45, 0, 11, -9]
# size = len(data)
# slectionSort(data, size)
# print('Sorted Array in Ascending Order:')
# print(data)


# A = [64, 25, 12, 22, 11]

# for i in range(len(A)):

#     min_idx = i
#     for j in range(i+1, len(A)):
#         if A[min_idx] > A[j]:
#             min_idx = j

#     A[j], A[min_idx] = A[min_idx], A[i]


# print("Sorted array")
# for i in range(len(A)):
#     print("%d" % A[i], end=" , ")

# def bubbleSort(arr):

#     n = len(arr)

#     for i in range(n):

#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]


# if __name__ == "__main__":
#     arr = [5, 1, 4, 2, 8]

#     bubbleSort(arr)

#     print("Sorted array is:")
#     for i in range(len(arr)):
#         print("%d" % arr[i], end=" ")


# def bubbleSort(array):

#     for i in range(len(array)):

#         for j in range(0, len(array) - i - 1):

#             if array[j] > array[j + 1]:

#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp


# data = [-2, 45, 0, 11, -9]

# bubbleSort(data)

# print('Sorted Array in Ascending Order:')
# print(data)


# def binarySearch(array, x, low, high):

#     while low <= high:

#         mid = low + (high - low)//2

#         if array[mid] == x:
#             return mid

#         elif array[mid] < x:
#             low = mid + 1

#         else:
#             high = mid - 1

#     return -1


# array = [3, 4, 5, 6, 7, 8, 9]
# x = 4

# result = binarySearch(array, x, 0, len(array)-1)

# if result != -1:
#     print("Element is present at index " + str(result))
# else:
#     print("Not found")
