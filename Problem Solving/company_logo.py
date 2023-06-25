from collections import Counter
s = input()
s = sorted(s)
s = Counter(s)
for item in s.most_common(3):
    print(item[0], item[1])
