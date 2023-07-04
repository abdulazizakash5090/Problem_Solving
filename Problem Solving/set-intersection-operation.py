n = int(input())
set_n = set(map(int, input().split()))
b = int(input())
set_b = set(map(int, input().split()))

print(len(set_b.intersection(set_n)))
