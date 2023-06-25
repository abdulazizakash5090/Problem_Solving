m = int(input())

a = set(map(int, input().split()))

n = int(input())

b = set(map(int, input().split()))

c = a.difference(b)
d = b.difference(a)

e = c.union(d)

RESULT = list(e)

RESULT.sort()

for i in range(len(RESULT)):
    print(RESULT[i])


m = input()
a = set(input().split(' '))
n = input()
b = set(input().split(' '))
intersect = sorted(list(map(int, (a-b).union(b-a))))
for i in intersect:
    print(i)
