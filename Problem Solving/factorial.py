num = 7

factorial = 1

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)


def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 7

result = factorial(num)
print("Thr factorial of", num, "is", result)


def fact(n):
    initial = 1
    for i in range(1, n+1):
        initial = initial * i
    return initial


result = fact(5)
print(result)
