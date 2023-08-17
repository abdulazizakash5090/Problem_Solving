strs = ["flower", "flow", "flight"]


for i in strs:
    s0 = strs[0].lower()
    s1 = strs[1].lower()
    s2 = strs[2].lower()
    common = set(s0) & set(s1) & set(s2)
    print(''.join(common))


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ("")
        if len(strs) == 1:
            return (strs[0])

        pref = strs[0]
        plen = len(pref)

        for s in strs[1:]:

            while pref != s[0:plen]:
                pref = pref[0:(plen-1)]
                plen -= 1

                if plen == 0:
                    return ("")

    def longestCommonPrefix(self, v: List[str]) -> str:
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first, len(last)))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]
        return ans
