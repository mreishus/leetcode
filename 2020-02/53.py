#!/usr/bin/env python

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_answer = nums[0]
        max_ending_here = 0
        for i, num in enumerate(nums):
            max_ending_here = max(max_ending_here + num, num)
            max_answer = max(max_answer, max_ending_here)
        return max_answer


if __name__ == "__main__":
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    answer = Solution().maxSubArray(A)
    print("Expect: 6")
    print(answer)
