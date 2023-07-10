n = int(input())
n_set = set(map(int, input().split()))
b = int(input())
b_set = set(map(int, input().split()))

result = len(n_set ^ b_set)
print(result)
