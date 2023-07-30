def print21argest(arr, arr_size):

    if (arr_size < 2):
        print(" Invalid Input ")
        return

    arr.sort

    for i in range(arr_size-2, -1, -1):

        if (arr[i] != arr[arr_size-1]):

            print("The second largest element is", arr[i])
            return

    print("There is no second largest element")

    arr = [12, 35, 1, 10, 34, 1]
    n = len(arr)
    print21argest(arr, n)


v = [12, 35, 1, 10, 34, 1]

s = set(v)

s = sorted(s)

print("The Second Largest Element in Vector is: ", s[-2])


def print21largest(arr, arr_size):

    if (arr_size < 2):
        print(" Invalid Input ")

    largest = second = -2454635434

    for i in range(0, arr_size):
        largest = max(largest, arr[i])

    for i in range(0, arr_size):
        if (arr[i] != largest):
            second = max(second, arr[i])
            print("There is no second " + "largest element")
        else:
            print("The second largest " + "element is \n", second)


arr = [12, 35, 1,
       10, 34, 1]
n = len(arr)
print21argest(arr, n)


def print2largest(arr, arr_size):

    if (arr_size < 2):

        print("Invalid Input ")
        return

    first = second = -2147483648
    for i in range(arr_size):

        if (arr[i] > first):
            second = first
            first = arr[i]

        elif (arr[i] > second and arr[i] != first):
            second = arr[i]

    if (second == -2147483648):
        print("There is no second largest element")
    else:
        print("The second largest element is", second)


arr = [12, 35, 1, 10, 34, 1]
n = len(arr)

print2largest(arr, n)
