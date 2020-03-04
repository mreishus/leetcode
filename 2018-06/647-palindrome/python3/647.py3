#!/usr/bin/env python3


class Solution:
    def expand_palin_count(self, s, i, j):
        count = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            count += 1
            i -= 1
            j += 1
        return count

    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.expand_palin_count(s, i, i)
            count += self.expand_palin_count(s, i, i + 1)
        return count


s = Solution()
print("Expect to see 6")
print(s.countSubstrings("aaa"))
