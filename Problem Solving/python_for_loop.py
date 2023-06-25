# fruits = ["apple", "banana", "cherry"]
#
# for x in fruits:
#     print(x)

# for x in "banana":
#     print(x)

# for x in fruits:
#     if x == "banana":
#         break
#     print(x)

# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)

# for x in range(6):
#     print(x)

# for x in range(2,6):
#     print(x)

# for x in range(2, 30, 3):
#     print(x)

# for x in range(6):
#     print(x)
# else:
#     print("Finally finised!")

# for x in range(6):
#     if x == 3: break
#     print(x)
# else:
#   print("Finally finished!")

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#     for y in fruits:
#         print(x,y)

# for x in [0, 1, 2]:
#     pass

# nums = (1, 2, 3, 4)
#
# sum_nums = 0
#
# for num in nums:
#     sum_nums = sum_nums + num
#
# print(f'Sum of numbers is {sum_nums}')

# words= ["Apple", "Banana", "Car", "Dolphin" ]
# for word in words:
#     # This loop is fetching word from the list
#     print("The following lines will print each letters of " + word)
#     for letter in word:
#         # This loop is fetching letter for the word
#         print(letter)
#     print("")  # This print is used to print a blank line

# nums = [1, 2, 3, 4, 5, 6]
#
# n = 2
#
# found = False
# for num in nums:
#     if n == num:
#         found = True
#         break
# print(f'List contains {n}: {found}')

# nums = [1, 2, -3, 4, -5, 6]
#
# sum_positives = 0
#
# for num in nums:
#     if num < 0:
#         continue
#     sum_positives += num
#
# print(f'Sum of Positive Numbers: {sum_positives}')

# def print_sum_even_nums(even_nums):
#     total = 0
#
#     for x in even_nums:
#         if x % 2 != 0:
#             break
#
#         total += x
#     else:
#         print("For loop executed normally")
#         print(f'Sum of numbers {total}')
#
#
# # this will print the sum
# print_sum_even_nums([2, 4, 6, 8])
#
# # this won't print the sum because of an odd number in the sequence
# print_sum_even_nums([2, 4, 5, 8])

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x,y)

# for i in range(2, 4):
#
#     # Printing inside the outer loop
#     # Running inner loop from 1 to 10
#     for j in range(1, 11):
#         # Printing inside the inner loop
#         print(i, "*", j, "=", i * j)
#     # Printing inside the outer loop
#     print()

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# ar = []
# p = 0
#
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if i+j+k != n:
#                 ar.append([])
#                 ar[p] = [i, j, k]
#                 p += 1
# print(ar)

# rows = int(input("Enter the # of rows: "))
# columns = int(input("Enter the # of columns "))
# symbol = input("Enter the # of symbol ")

# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()


# for _ in range(int(input())):
#     name = input()
#     score = float(input())

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x, y)


# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end=' ')
#     print()

# rows = 5

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print('')

# n = int(input().strip())

# for i in range(n):

#     # Printing inside the outer loop
#     # Running inner loop from 1 to 10
#     for j in range(1, 11):
#         # Printing inside the inner loop
#         print(i, "*", j, "=", i * j)
#     # Printing inside the outer loop
#     print()

# n = int(input().strip())

# for i in range(1, 11):
#     s = n * i
#     print(n, "x", i, "=", s)

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# l = []

# print([[i, j, k] for i in range(x+1) for j in range(y+1)
#        for k in range(z+1) if i+j+k != n])

# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i + j + z == n:
#                 continue
#             print(l(append(n)))
# print()

# lst = [1, 4, 3, 2]
# print(list(reversed(lst)))

# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     for i in reversed(arr):
#         print(i, end=' ')

# phonelist = {}

# n = int(input())
# for i in range(n):
#     name = input()
#     number = int(input())
#     phonelist = + {name, number}
#     print(phonelist)

# n = int(input())

# phone_book = {}

# for i in range(n):
#     name, phone_number = input().split()
#     phone_book[name] = phone_number

# while True:
#     try:
#         query = input()
#         phone_number = phone_book.get(query, False)
#         if phone_number:
#             print("{}={}", format(query, phone_number))
#         else:
#             print("Not Found")
#     except EOFError:
#         break


# n = int(input())

# phone_book = {}

# for i in range(n):
#     name, phone_number = input().split()
#     phone_book[name] = phone_number

# while True:
#     try:
#         name = input()
#         if name in phone_book:
#             print(name + "=" + phone_book[name])
#         else:
#             print("Not found")
#     except:
#         break

# if n <= 1:
#     return 1
# else:
#     return n * factorial(n-1)


# n = int(input())
# DATA = bin(n)

# MAXIMUN = 0
# CURRENT = 0

# for num in DATA:
#     if num == '1':
#         CURRENT = CURRENT + 1
#     else:
#         MAXIMUN = max(MAXIMUN, CURRENT)
#         CURRENT = 0

# print(max(MAXIMUN, CURRENT))


n = int(input())

# phone_book = {}

# for i in range(n):
#     name, phone_number = input().split()
#     phone_book[name] = phone_number
# while True:
#     try:
#         name = input()
#         if name in phone_book:
#             print(name + "=" + phone_book[name])
#     except:
#         break
