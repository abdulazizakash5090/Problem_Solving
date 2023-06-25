from collections import OrderedDict

num = int(input())
dict = OrderedDict()

for i in range(num):
    item_name = input()
    net_price = int(input())

    dict[item_name] = net_price


print(dict)

n = int(input())
d = OrderedDict()

for i in range(n):
    item, space, number = input().rpartition(' ')
    number = int(number)
    if item in d.keys():
        d[item] += number
    else:
        d[item] = number

for i in d.keys():
    print(i, d[i])


d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)

for item, quantity in d.items():
    print(item, quantity)
