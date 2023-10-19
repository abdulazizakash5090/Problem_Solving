import math

number = int(input())

print(f'math.sqrt({number:.1f})')


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        first, last = 1, x
        while first <= last:
            mid = first + (last-first) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1
        return last


class Solution:
    def mySqrt(self, x: int) -> int:
        number = 1
        while number*number <= x:
            number += 1
        return number


class Solution:
    def mySqrt(selg, s: int) -> int:
        x = sqrt(s)
        if x % 1 < 0.5:
            return round(x)
        else:
            return round(x-0.5)
