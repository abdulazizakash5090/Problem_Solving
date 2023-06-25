# n = int(input())
# integer_list = map(int, input().split())
# tup = ()
# for x in integer_list:
#     tup += (x, )

# print(hash(tup))
# if __name__ == '__main__':
#     n = int(input())
# interger_tuple = tuple(map(int, input().split()))
# print(hash(interger_tuple))

# n = int(input())
# integer_list = map(int, input().split())
# tupl = tuple(integer_list)
# print(hash(tupl))

n = int(input().strip())
t = tuple(int(item) for item in input().split())
print(hash(t))
