#!/usr/bin/env python

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        max_ending_here = 0
        for num in nums:
            max_ending_here = max(num, num + max_ending_here)
            max_sum = max(max_sum, max_ending_here)
        return max_sum


if __name__ == "__main__":
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    answer = Solution().maxSubArray(A)
    print("Expect: 6")
    print(answer)
