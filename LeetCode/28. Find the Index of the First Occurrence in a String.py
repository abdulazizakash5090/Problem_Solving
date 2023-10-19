# haystack = "leetcode"
# needle = "leeto"

# if needle in haystack:
#     print(0)
# else:
#     print(-1)


# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:

#     if needle == "":
#         return 0

#     for i in range(len(haystack) + 1) - len(needle):
#         for j in range(len(needle)):
#             if haystack[i+j] != needle[j]:
#                 break
#             if j == len(needle) - 1:
#                 return i

#     return -1

#     for i in range(len(haystack)+1 - len(needle)):
#         if haystack[i:i + len(needle)] == needle:
#             return i
#     return -1


# def strStr(haystack, needle):
#     m = len(haystack)
#     n = len(needle)

#     for i in range(m - n + 1):
#         if haystack[i:i + n] == needle:
#             return i

#     return -1


# haystack = "sadbutsad"
# needle = "sad"

# result = strStr(haystack, needle)
# print(result)
# Source
# https://www.geeksforgeeks.org/python-first-character-occurrence-from-rear-string/
