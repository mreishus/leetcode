#!/usr/bin/env python


from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        results = []
        target = {}
        for char in p:
            if char in target:
                target[char] += 1
            else:
                target[char] = 1

        window = {}
        for j in range(len(p)):
            if j >= len(s):
                break
            if s[j] in window:
                window[s[j]] += 1
            else:
                window[s[j]] = 1

        if window == target:
            results.append(0)

        for i in range(1, len(s) - len(p) + 1):
            j = i + len(p)
            window[s[i - 1]] -= 1
            if window[s[i - 1]] == 0:
                del window[s[i - 1]]
            if s[j - 1] in window:
                window[s[j - 1]] += 1
            else:
                window[s[j - 1]] = 1
            # print(window)
            # print(target)
            # print(" ")
            if window == target:
                results.append(i)
                # print("Found match")
            # print("??")
            # print(s[i - 1])
            # print(s[j - 1])
        return results


if __name__ == "__main__":
    cases = [("cbaebabacd", "abc", [0, 6]), ("abab", "ab", [0, 1, 2])]
    for (s, p, want) in cases:
        got = Solution().findAnagrams(s, p)
        print(f"Passed? {want == got} | got {got} want {want} | s {s} p {p}")
