N, M = map(int, input().split())
athletes = []
for i in range(N):
    list(map(int, input().split()))
    athletes.append(athletes)
K = int(input())
athletes.sort(key=lambda x: x[K])
for athlete in athletes:
    print(*athlete)
