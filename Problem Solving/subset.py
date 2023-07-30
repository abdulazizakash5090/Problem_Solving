T = int(input())

for i in range(T):
    SA = int(input())
    set_A = set(map(int, input().split()))
    SB = int(input())
    set_B = set(map(int, input().split()))

    if set_A.issubset(set_B):
        print(True)
    else:
        print(False)
