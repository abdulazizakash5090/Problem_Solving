import sys


def print3largest(arr, arr_size):

    if (arr_size < 3):

        print(" Invalid Input")
        return

    third = first = second = -sys.maxsize

    for i in range(0, arr_size):

        if (arr[i] > first):

            third = second
            second = first
            first = arr[i]

        elif (arr[i] > second):

            third = second
            second = arr[i]

    print("Three largest elements are", first, second, third)


arr = [12, 13, 1, 10, 34, 1]
n = len(arr)
print3largest(arr, n)


def find3largest(arr, n):
    arr = sorted(arr)

    check = 0
    count = 1

    for i in range(1, n + 1):

        if (count < 4):
            if (check != arr[n-i]):

                print(arr[n - i], end=" ")
                check = arr[n - i]
                count += 1

            else:
                break


arr = [12, 45, 1, -1, 45,
       54, 23, 5, 0, -10]

n = len(arr)
find3largest(arr, n)


V = [11, 65, 193, 36, 209, 664, 32]
V.sort()
V.reverse()

print(f"first = {V[0]}")
print(f"second = {V[1]}")
print(f"third = {V[2]}")
