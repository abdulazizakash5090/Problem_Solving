class Soluion:
    def climStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climStairs(n-1) + self.climStairs(n-2)


def climStairs(self, n):
    prev1 = 1
    prev2 = 0
    for i in range(1, n+1):
        curi = prev1 + prev2
        prev2 = prev1
        prev1 = curi
    return prev1


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one
