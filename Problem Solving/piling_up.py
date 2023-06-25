from collections import deque
ANS = []
T = int(input())

for _ in range(T):
    n = int(input())
    sl = list(map(int, input().split()))

    for _ in range(n-1):
        if sl[0] >= sl[len(sl)-1]:
            a = sl[0]
            sl.pop(0)
        elif sl[0] < sl[len(sl)-1]:
            a = sl[len(sl)-1]
            sl.pop(len(sl)-1)
        else:
            pass

        if len(sl) == 1:
            ANS.append("Yes")

        if ((sl[0] > a) or (sl[len(sl)-1] > a)):
            ANS.append("No")
            break

print("\n".join(ANS))


for _ in range(int(input())):
    _, queue = input(), deque(map(int, input().split()))
    for cube in reversed(sorted(queue)):
        if queue[-1] == cube:
            queue.pop()
        elif queue[0] == cube:
            queue.popleft()
        else:
            print("No")
            break
    else:
        print('Yes')
