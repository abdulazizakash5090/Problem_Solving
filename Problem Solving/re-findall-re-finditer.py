# import re
# S = input()
# if re.findall(r"\B[AEIOUaeiou]{2,}\B[^AEIOUaeiou]", S):
#     for i in re.findall(r"\B[AEIOUaeiou]{2,}\B[^AEIOUaeiou]", S):
#         print(i[:-1])
# else:
#     print(-1)

import re
S, K = input(), input()
pat = re.compile(S)
m = pat.search(S)

if m:
    while m:
        print((m.start(), m.end()-1))
        i = m.start() + 1
        m = pat.search(S, i)
else:
    print((-1, -1))


for _ in range(int(input())):
    line = input()
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: [
          'or', 'and'][x.group() == '&&'], line))
