n = input()
set_n = set(map(int, input().split()))
b = input()
set_b = set(map(int, input().split()))

print(len(set_b.union(set_n)))


# More than 2 lines will result in 0 score. Do not leave a blank line also
for i in range(1, int(input())+1):
    print(i)
