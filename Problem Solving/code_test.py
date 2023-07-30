# def performOperation(secondInter, secondDecimal, secondString):
#     firstInterger = 4

#     firstDecimal = 4.0

#     firstString = 'HackRank'

#     print(firstInterger + int(secondInter))
#     print(firstDecimal + int(secondDecimal))
#     print(firstString + (secondString))


# n = int(input())

# if n % 2 == 0:
#     print("Weird")
# elif (n <= 2) and (n >= 5):
#     print("Not Weird")
# elif (n <= 6) and (n >= 20):
#     print('Weird')
# else:
#     print("Not Weird")

# n = int(input())
# if (n % 2 != 0) or (n >= 6 and n <= 20):
#     print("Weird")
# else:
#     print("Not Weird")

# n = int(input())

# for i in range(n):
#     print(i*i)

# def is_leap(year):
#     leap = False

#     # Write your logic here

#     if (year % 100 == 0) and (year % 400 != 0):
#         return False
#     elif (year % 4 == 0):
#         leap = True
#     return leap


# year = int(input())
# print(is_leap(year))

# n = int(input())

# for i in range(1, n+1):
#     print(i)

# rows = int(input("Enter the # of rows: "))
# columns = int(input("Enter the # of columns: "))
# symbol = input("Enter a symbol to use: ")

# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()

# n = int(input())
# arr = map(int, input().split())

# print(sorted(set(arr), reverse=True)[1])

# result = []
# scores = []

# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     result += [[name, score]]
#     # print(result)
#     scores += [score]
#     # print(scores)
#     b = sorted(list(set(scores)))[1]
#     # print(b)

#     for a, c in sorted(result):
#         if c == b:
#             print(a)


# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     if query_name in student_marks:
#         print("%.02f" % (sum(student_marks[query_name])/3))


# print("Number Pattern")

# row = 5

# for i in range(1, row+1, 1):
#     for j in range(1, i+1):
#         print(j, end=' ')

#     print("")


# s = 0
# n = int(input("Enter number "))

# for i in range(1, n+1, 1):
#     s += i
# print("\n")
# print("Sum is: ", s)


# n = 2

# for i in range(1, 11, 1):
#     product = n * i
#     print(product)

# n = int(input().split())
# if (n % 2 != 0) or (n >= 6 and n <= 20):
#     print("Weird")
# else:
#     print("Not Weird")

# if n % 2 == 0:
#     if 2 <= n <= 5 or n > 20:
#         print("Not Weird")
#     else:
#         pass
# else:
#     print("Weird")


# n = int(input().split())

# if n % 2 == 1:
#     print("Werid")
# elif n % 2 == 0 and n in range(2, 5):
#     print("Not Werid")
# elif n % 2 == 0 and n in range(6, 21):
#     print("Weird")
# else:
#     pass

# n = int(input())

# for i in range(1, n):
#     print(i*i)

def is_leap(year):
    leap = False

    if (year % 100 == 0) and (year % 400 != 0):
        leap = False
    elif (year % 4 == 0):
        leap = True
    return leap


# if year % 4 == 0:
#     leap = True
# if year % 100 == 0:
#     leap = False
# if year % 400 == 0:
#     leap = True


# def is_leap(year):
#     leap = False

#     if (year % 100 == 0) and (year % 400 != 0):
#         leap = False
#     elif (year % 4 == 0):
#         leap = True
#     return leap


# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# arr = []
# p = 0


# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if x + y + z != n:
#                 arr.append([])
#                 arr[p] = [i, j, k]
#                 p += 1
# print(arr)

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# arr = []
# p = 0

# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if x + y + z != n:
#                 arr.append([])
#                 arr[p] = [i, j, k]
#                 p += 1

# print(arr)


# arr = [1, 2, 0, 4, 3, 0, 5, 0]

# arr.sort()

# arr.reverse()

# print(arr)

print(i*int((10**i-1)/9))
