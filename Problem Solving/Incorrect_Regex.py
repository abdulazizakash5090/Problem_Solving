# import re

# t = int(input())

# for i in range(t):
#     s = input()
#     try:
#         re.compile(s)
#         print("True")
#     except re.error:
#         print("False")

# import re
# for _ in range(int(input())):
#     ans = True
#     try:
#         reg = re.compile(input())
#     except re.error:
#         ans = False
#     print(ans)

# import re
# T = int(input())
# if 0 < T < 100:
#     for _ in range(T):
#         string = input()
#         try:
#             re.compile(string)
#             print(True)
#         except re.error:
#             print(False)


# import re
# T = int(input())
# for i in range(0, T):
#     regex_raw = input()
#     try:
#         regex = re.compile(regex_raw)
#     except re.error:
#         print(False)
#     else:
#         print(True)

import re

for t in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except:
        print(False)
