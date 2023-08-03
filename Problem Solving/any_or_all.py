# n = int(input())
# arr = map(int, input().split())

# print(any(arr))
# print(all(arr))

N = int(input())
numbers = list(map(int, input().split()))
print(all([x > 0 for x in numbers]) and any(
    [str(x) == str(x)[::-1] for x in numbers]))
