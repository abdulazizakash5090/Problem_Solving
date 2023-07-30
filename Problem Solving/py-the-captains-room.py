
from collections import Counter
K = int(input())
rooms = list(map(int, input().split()))
num_count = Counter(rooms)
print(num_count)
for n, c in num_count.items():
    if c == 1:
        print(n)
