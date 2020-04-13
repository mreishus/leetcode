#!/usr/bin/env python
"""
Given a binary array, find the maximum length of a contiguous subarray with
equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        seen = {}
        seen[0] = -1
        max_len = 0
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            elif num == 1:
                count += 1
            else:
                raise ValueError("Unexpected value")
            if count in seen:
                l = i - seen[count]
                max_len = max(max_len, l)
            else:
                seen[count] = i
        return max_len


if __name__ == "__main__":
    print("525")
    print("Expect: 1")
    got = Solution().findMaxLength([0, 1])
    print(got)
    assert got == 2
    print("Expect: 2")
    got = Solution().findMaxLength([0, 1, 0])
    print(got)
