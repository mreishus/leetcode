#!/usr/bin/env python
"""
387. First Unique Character in a String
Easy

Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.

"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, char in enumerate(s):
            if counts[char] >= 2:
                continue
            return i
        return -1
