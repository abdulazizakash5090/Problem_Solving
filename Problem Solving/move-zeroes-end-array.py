def pushZerosToEnd(arr, n):
    count = 0

    for i in range(n):
        if arr[i] != 0:

            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1


arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)

A = [5, 6, 0, 4, 6, 0, 9, 0, 8]
n = len(A)
j = 0
for i in range(n):
    if A[i] != 0:
        A[j], A[i] = A[i], A[j]
        j += 1
print(A)


arr = [5, 6, 0, 4, 6, 0, 9, 0, 8]

nonZeroValues = [x for x in arr if x != 0]

zeroes = [j for j in arr if j == 0]

arr = nonZeroValues + zeroes

print("array after shifting zeros to right side: ", arr)


A = [5, 6, 0, 4, 6, 0, 9, 0, 8]
n = len(A)
B = [0] * n
j = 0
count = 0

for i in range(n):
    if A[i] != 0:
        B[j] = A[j]
        j += 1
    else:
        count += 1

while count > 0:
    B[j] = 0
    count -= 1
    j += 1

for i in range(n):
    A[i] = B[i]

for i in range(n):
    print(A[i], end=" ")
