#!/usr/bin/env python

"""
560. Subarray Sum Equals K
Medium

Given an array of integers and an integer k, you need to find the total number
of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:

    The length of the array is in range [1, 20,000].  The range of numbers in
    the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums_seen = defaultdict(int)
        sums_seen[0] = 1
        total = 0
        count = 0
        for i, num in enumerate(nums):
            total += num

            want_left = total - k
            # print(f"Want Left: {want_left} Sums_seen: {sums_seen}")
            if want_left in sums_seen:
                # print(f"   Adding {sums_seen[want_left]}")
                count += sums_seen[want_left]

            sums_seen[total] += 1

        return count


if __name__ == "__main__":
    print("560 Subarray Sum Equals K")
    cases = [
        ([1, 1, 1], 2, 2),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 55),
    ]
    for (A, k, want) in cases:
        got = Solution().subarraySum(A, k)
        print(f"Pass? {got == want} | got {got} | want {want} | A {A}")
