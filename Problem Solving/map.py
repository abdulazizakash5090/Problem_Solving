def myfunc(n):
    return len(n)


x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)
print(list(x))


def myfunc(a, b):
    return a + b


x = map(myfunc, ('apple', 'banana', 'cherry'),
        ('orange', 'lemon', 'pineapple'))

print(x)
print(list(x))


def addition(n):
    return n + n


numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

l = ['sat', 'bat', 'cat', 'mat']

test = list(map(list, l))
print(test)


def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num


numbers = [1, 2, 3, 4, 5]

result = list(map(double_even, numbers))

print(result)


numbers = [2, 4, 6, 8, 10]


def square(number):
    return number * number


squared_numbers_iterator = map(square, numbers)

squared_number = list(squared_numbers_iterator)
print(squared_number)


def calculateSquare(n):
    return n*n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)


def calculateSquare(n):
    return n*n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

numbersSquare = set(result)
print(numbersSquare)

numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

numbersSquare = set(result)
print(numbersSquare)

num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))
