from typing import List


# def isPairSum(A, N, X):

#     for i in range(N):
#         for j in range(N):

#             if (i == j):
#                 continue

#             if (A[i]+A[j] == X):
#                 return True

#             if (A[i]+A[j] > X):
#                 break

#     return 0


# arr = [2, 3, 5, 8, 9, 10, 11]
# val = 17

# print(isPairSum(arr, len(arr), val))


def isPairSum(A: List[int], N: int, X: int) -> bool:

    i = 0
    j = N - 1

    while i < j:
        if A[i] + A[j] == X:
            return True

        elif A[i] + A[j] < X:
            i += 1

        else:
            j -= 1

    return False


# Driver code
if __name__ == "__main__":
    # array declaration
    arr = [2, 3, 5, 8, 9, 10, 11]

    # value to search
    val = 17

    arrSize = len(arr)

    arr.sort()

    print(isPairSum(arr, arrSize, val))


def two_sum(arr, target):

    pointer_one = 0
    pointer_two = len(arr) - 1

    while pointer_one < pointer_two:
        if sum == target:
            return True
        elif sum < target:
            pointer_one += 1
        else:
            pointer_two -= 1

    return False


print(two_sum([1, 3, 4, 8, 9], 11))


def reverseArray(array):
    start, end = 0, len(array)-1
    while start < end:
        start += 1
        end - 1


array = [10, 20, 30, 40, 50]
reverseArray(array)
print(array)
