import collections


def count_occurence(words):

    counts = dict()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return [str(i) for i in counts.values()]


n = input()
l = [input() for _ in range(int(n))]

print(len(set(l)))
print(" ".join(count_occurence(l)))


N = int(input())
d = collections.OrderedDict()

for i in range(N):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(len(d))

for k, v in d.items():
    print(v, end=" ")
