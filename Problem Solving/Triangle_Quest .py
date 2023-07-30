n = 3
for i in range(n+1):
    print(i*"*")

n = 3
for i in range(n+1):
    print((2*i-1)*"*")

n = 6

for i in range(n+1):
    print(i*"*")

n = int(input("Enter how many row: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

rows = int(input("Enter number of row: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
print("\n")

rows = int(input("Enter number of row: "))

ascii_value = 65

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value += 1
    print("\n")

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    print("\n")


rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1+i+1):
        print(j, end=" ")

    print("\n")
