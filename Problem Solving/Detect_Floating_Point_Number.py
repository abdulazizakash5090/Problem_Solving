import re

T = int(input())

for i in range(T):
    temp = input()
    resultat = bool(re.match(r"^[+-]?[0-9]*\.?[0-9]+$", temp))
    if temp == '0':
        print(False)
    else:
        print(resultat)
