#!/usr/bin/env python

"""
Given two strings text1 and text2, return the length of their longest common
subsequence.

A subsequence of a string is a new string generated from the original string
with some characters(can be none) deleted without changing the relative order
of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec"
                              is not). A common subsequence of two strings is a
subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" Output: 3  Explanation: The longest
common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc" Output: 3 Explanation: The longest common
subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def" Output: 0 Explanation: There is no such
common subsequence, so the result is 0.
"""

import functools


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        DP is much faster than recursive here, even with LRU_Cache..
        """
        len1 = len(text1)
        len2 = len(text2)
        DP = []
        for i in range(len1 + 1):
            DP.append([0] * (len2 + 1))

        for i in range(len1):
            for j in range(len2):
                if text1[i] == text2[j]:
                    DP[i + 1][j + 1] = 1 + DP[i][j]
                else:
                    DP[i + 1][j + 1] = max([DP[i][j + 1], DP[i + 1][j]])

        return DP[-1][-1]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        @functools.lru_cache(None)
        def helper(i, j):
            if i < 0 or j < 0:
                return 0

            if text1[i] == text2[j]:
                return 1 + helper(i - 1, j - 1)

            return max([helper(i - 1, j), helper(i, j - 1)])

        return helper(len(text1) - 1, len(text2) - 1)


if __name__ == "__main__":
    cases = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("bl", "yby", 1),
    ]
    for (s1, s2, want) in cases:
        got = Solution().longestCommonSubsequence(s1, s2)
        print(f"Pass? {want == got} | got {got} | want {want} | s1 {s1} | s2 {s2}")
