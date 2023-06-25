from collections import deque

d = deque()

for _ in range(int(input())):
    args = input().split()
    if (args[0] == 'append'):
        d.append(args[1])
    elif (args[0] == 'appendleft'):
        d.appendleft(args[1])
    elif (args[0] == 'pop'):
        d.pop()
    elif (args[0] == 'popleft'):
        d.popleft()

print(' '.join(d))
