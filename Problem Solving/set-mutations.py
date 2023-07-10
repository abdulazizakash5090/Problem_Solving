# a = int(input())
# a_set = set(map(int, input().split()))

# n = int(input())

# for i in range(n):
#     name = input().split()
#     if name[0] == "intersection_update":
#         a_set.intersection_update(int(a_set[1]))
#     elif name[0] == "update":
#         a_set.update(int(a_set[1]))
#     elif name[0] == "symmetric_difference_update":
#         a_set.symmetric_difference_update(int(a_set[1]))
#     elif name[0] == "difference_update":
#         a_set.difference_update(int(a_set[1]))

# print(a_set)


A = int(input())
set_A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    a = input().split()
    set_N = set(map(int, input().split()))
    if a[0] == "intersection_update":
        set_A.intersection_update(set_N)
    elif a[0] == "update":
        set_A.update(set_N)
    elif a[0] == "symmetric_difference_update":
        set_A.symmetric_difference_update(set_N)
    elif a[0] == "difference_update":
        set_A.difference_update(set_N)

print(sum(set_A))
