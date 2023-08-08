class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]

        return ans


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
        number = 0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[(i+1)]]:
                number -= roman[s[i]]
            else:
                number += roman[s[i]]
        return number + roman[s[-1]]


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace(
            "XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")

        return sum(map(lambda x: roman_to_integer[x], s))
