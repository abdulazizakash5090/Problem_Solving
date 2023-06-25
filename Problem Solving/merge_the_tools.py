# def merge_the_tools(string, k):
#     n = len(string)

#     def help_fun(items):
#         seen = set()
#         for i in items:
#             if i not in seen:
#                 yield i
#                 seen.add(i)

#     while string:
#         word = string[0:k]
#         string = string[k:]

#         print(''.join(help_fun(word)))


# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)


def mergeSort(array):
    if len(array) > 1:

        r = len(array) // 2
        L = array[:r]
        M = array[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[i]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)
