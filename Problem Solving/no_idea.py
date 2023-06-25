# N = input().split()
# M = input().split()
# A = set(input().split())
# B = set(input().split())

# COUNTER = 0

# for i in M:
#     if i in A:
#         COUNTER += 1
#     if i in B:
#         COUNTER -= 1

# print(COUNTER)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

happiness = 0

for e in arr:
    if e in s1:
        happiness += 1
    elif e in s2:
        happiness -= 1

    else:
        None
print(happiness)
