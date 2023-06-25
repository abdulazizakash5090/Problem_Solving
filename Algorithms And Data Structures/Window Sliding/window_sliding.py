# code
import sys

# O(n * k) solution for finding
# maximum sum of a subarray of size k
INT_MIN = -sys.maxsize - 1

# Returns maximum sum in a
# subarray of size k.


def maxSum(arr, n, k):

    # Initialize result
    max_sum = INT_MIN

    # Consider all blocks
    # starting with i.
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]

        # Update result if required.
        max_sum = max(current_sum, max_sum)

    return max_sum


# Driver code
arr = [1, 4, 2, 10, 2,
       3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))

# This code is contributed by mits


def maxSum(arr, k):
    # length of the array
    n = len(arr)

    # length of array must be greater
    # window size
    if n < k:
        print("Invalid")
        return -1

    # sum of first k elements
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # remove the  first element of previous
    # window and add the last element of
    # the current window to calculate the
    # the sums of remaining windows by
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum


arr = [16, 12, 9, 19, 11, 8]
k = 3
print(maxSum(arr, k))
