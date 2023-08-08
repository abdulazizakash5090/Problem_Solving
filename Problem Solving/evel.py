number = 9

square_number = eval('number * number')
print(square_number)

x = 1
print(eval('x+1'))


def calculatePerimeter(l):
    return 4*l


def calculateArea(l):
    return l*l


expression = input("Type a function: ")

for l in range(1, 5):
    if (expression == 'calculatePerimeter(l)'):
        print("If length is ", l, "Perimeter =", eval(expression))
    elif (expression == 'calculateArea(l)'):
        print("If length is ", l, ", Area = ", eval(expression))
    else:
        print('Wrong Function')
        break
