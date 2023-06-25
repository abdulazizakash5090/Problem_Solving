num = [1, 2, 3, 4, 5]

result = [x*x for x in num]
print(result)

x = int(input())
y = int(input())
z = int(input())
n = int(input())
ar = []
p = 0

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                ar.append([])
                p += 1

print(ar)

ans = [[i, j, k] for i in range(x+1) for j in range(y+1)
       for k in range(z+1) if i + j + k != n]

print(ans)
