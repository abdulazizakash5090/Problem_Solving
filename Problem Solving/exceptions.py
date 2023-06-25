n = int(input())

for i in range(n):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except (ZeroDivisionError, ValueError) as e:
        print('Error Code', e)


# try:
#     a = 3
#     b = 1
#     print(a/b)
# except ZeroDivisionError as e:
#     print("Error: Cannot divide by zero")
