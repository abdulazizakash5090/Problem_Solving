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


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        print("%.02f" % (sum(student_marks[query_name])/3))
