#!/usr/bin/env python

"""
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.
"""

from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen = set(arr)
        return sum(1 for x in arr if (x + 1) in seen)


if __name__ == "__main__":
    A = [1, 3, 2, 3, 5, 0]
    want = 3
    got = Solution().countElements(A)
    print(f"Pass? {want == got} | Want {want} | Got {got} | Input {A}")
