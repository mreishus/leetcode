#!/usr/bin/env python
"""
567. Permutation in String
Medium

Given two strings s1 and s2, write a function to return true if s2 contains the
permutation of s1. In other words, one of the first string's permutations is
the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:

    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].
"""


from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        target = Counter(s1)
        tester = Counter(s2[0 : len(s1)])
        if tester == target:
            return True

        for i in range(1, len(s2)):
            if i + len(s1) > len(s2):
                break
            left = i - 1
            right = i + len(s1) - 1
            leftc = s2[left]
            rightc = s2[right]

            tester[leftc] -= 1
            if tester[leftc] == 0:
                del tester[leftc]
            tester[rightc] += 1

            if tester == target:
                return True
        return False


if __name__ == "__main__":
    print("567 Permutation in string")
    cases = [("ab", "eidbaooo", True), ("ab", "eidboaoo", False)]
    for (s1, s2, want) in cases:
        got = Solution().checkInclusion(s1, s2)
        print(f"Pass? {got == want} | got {got} want {want} | {s1} {s2}")
