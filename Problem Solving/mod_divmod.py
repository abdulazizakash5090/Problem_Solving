a = int(input())
b = int(input())

division = a//b
modulo = a % b
divmods = divmod(a, b)

print(division, modulo, divmods, sep='\n')

a, b = int(input()), int(input())
print(a//b, a % b, divmod(a, b), sep='\n')
