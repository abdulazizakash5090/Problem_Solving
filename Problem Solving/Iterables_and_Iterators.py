from itertools import combinations

c = 0
N = int(input())
n = input().split()
K = int(input())
l = len(list(combinations(n, K)))
for i in combinations(n, K):
    if 'a' in i:
        c += 1

print(f"{c/l:.3f}")
