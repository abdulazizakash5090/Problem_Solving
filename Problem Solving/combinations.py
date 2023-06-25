from itertools import combinations_with_replacement

S, K = input().split()
K = int(K)
S = sorted(list(S))

for combination in combinations_with_replacement(S, K):
    print("".join(combination))
