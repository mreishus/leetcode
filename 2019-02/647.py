#!/usr/bin/env python


from typing import List


class Solution:
    def expand_palindromes(self, s: str, i: int, j: int) -> int:
        count = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            count += 1
            i -= 1
            j += 1
        return count

    def countSubstrings(self, s: str) -> int:
        count = 0
        for i, _ in enumerate(s):
            count += self.expand_palindromes(s, i, i)
            count += self.expand_palindromes(s, i, i + 1)
        return count


if __name__ == "__main__":
    print("hi")
    S = Solution()
    print("Expect: 6")
    print(S.countSubstrings("aaa"))
