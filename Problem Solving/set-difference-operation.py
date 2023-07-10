n = int(input())
set_n = set(map(int, input().split()))
b = int(input())
set_b = set(map(int, input().split()))

result = len(set_n-set_b)
print(result)
