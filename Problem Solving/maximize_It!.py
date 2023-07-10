# import sys
# from itertools import product

# k, m = map(int, input().split())
# user_input = sys.stdin.readlines()
# l = []

# for i in user_input:
#     i = i.split()
#     j = [int(x)**2 for x in i]
#     l.append(j)

# result = list(product(*l))
# sum_result = [(sum(x) % m) for x in result]
# print(max(sum_result))

import itertools

k, m = map(int, input().split())

L = [list(map(int, input().split()))[1:] for i in range(k)]

result = 0

for i in itertools.product(*L):
    r = 0
    for n in i:
        r += n**2

        if result < r % m:
            result = r % m
print(result)
