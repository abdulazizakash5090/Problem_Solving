lst = []

n = int(input())
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'insert':
        lst.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'print':
        print(lst)
    elif cmd[0] == 'remove':
        print(lst)
    elif cmd[0] == 'append':
        print(lst)
    elif cmd[0] == 'sort':
        print(lst)
    elif cmd[0] == 'pop':
        print(lst)
    else:
        lst.append()