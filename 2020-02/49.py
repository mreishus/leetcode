#!/usr/bin/env python

from typing import List
from collections import defaultdict, Counter

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        groups = []
        for a_str in strs:
            counts = str(sorted(a_str))
            if counts in seen:
                # Seen before
                i = seen[counts]
                groups[i].append(a_str)
            else:
                # New
                groups.append([a_str])
                seen[counts] = len(groups) - 1
        return groups

    def groupAnagramsSlow(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(int)
        groups = []
        for a_str in strs:
            counts = frozenset(Counter(a_str).items())
            if counts in seen:
                # Seen before
                i = seen[counts]
                groups[i].append(a_str)
            else:
                # New
                groups.append([a_str])
                seen[counts] = len(groups) - 1
        return groups


if __name__ == "__main__":
    A = ["eat", "tea", "tan", "ate", "nat", "bat"]
    A = [
        "hos",
        "boo",
        "nay",
        "deb",
        "wow",
        "bop",
        "bob",
        "brr",
        "hey",
        "rye",
        "eve",
        "elf",
        "pup",
        "bum",
        "iva",
        "lyx",
        "yap",
        "ugh",
        "hem",
        "rod",
        "aha",
        "nam",
        "gap",
        "yea",
        "doc",
        "pen",
        "job",
        "dis",
        "max",
        "oho",
        "jed",
        "lye",
        "ram",
        "pup",
        "qua",
        "ugh",
        "mir",
        "nap",
        "deb",
        "hog",
        "let",
        "gym",
        "bye",
        "lon",
        "aft",
        "eel",
        "sol",
        "jab",
    ]
    got = Solution().groupAnagrams(A)
    print(got)
    got = Solution().groupAnagramsSlow(A)
    print(got)
