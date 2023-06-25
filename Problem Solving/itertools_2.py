from itertools import permutations

word, length = input(). split()
chars = sorted(word)

for c in permutations(chars, int(length)):
    print("".join(c))


s, k = input().split()
l = sorted(list(permutations(s, int(k))))
for i in l:
    print("".join(i))
