def minion_game(string):

    # your code goes here
vv = 'AEIOU'
l = len(s)
c = 0
v = 0
for i in range(l):
    if s[i] in vv:
        v += l-i
    else:
        c += l-i
if c > v:
    print('Stuart', c)
elif c == v:
    print("Draw")
else:
    print('Kevin', v)


s = input()
minion_game(s)
