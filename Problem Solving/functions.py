def calculate_total(exp):
    total = 0
    for item in exp:
        total = total+item
    return total


toms_total = tom_exp_list = [2100, 3400, 3500]
joess_total = joes_exp_list = [200, 300, 500]

print("Tom's total expenses:", toms_total)
print("Joes's total expenses:", joess_total)


def sum(a, b):
    print("a:", a)
    print("b:", b)
    total = a+b
    print("total inside function:", total)
    return total


n = sum(5, 6)
print("Total outside function:", n)


def sum(a, b=0):
    print("a:", a)
    print("b:", b)
    total = a+b
    print("total inside function:", total)
    return total


n = sum(5, 6)
print("Total outside function:", n)
