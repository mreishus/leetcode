#!/usr/bin/env python
"""
Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

from typing import List
import functools

# cases = [([2, 3, 1, 1, 4], True), ([3, 2, 1, 0, 4], False), (big_case, True)]


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump_amount in enumerate(nums):
            if i > max_reach:
                return False
            reach_here = i + jump_amount
            max_reach = max(reach_here, max_reach)
        return True

    def canJump_too_slow(self, nums: List[int]) -> bool:
        target = len(nums) - 1

        @functools.lru_cache(None)
        def helper(loc):
            if loc > target:
                return False
            if loc == target:
                return True

            val = nums[loc]
            return any(helper(loc + jump) for jump in range(1, val + 1))

        return helper(0)


if __name__ == "__main__":
    print("55 Jump Game")
    cases = [([2, 3, 1, 1, 4], True), ([3, 2, 1, 0, 4], False)]
    for (A, want) in cases:
        got = Solution().canJump(A)
        print(f"Pass? {want == got} | Got {got} | Want {want} | Nums {A}")
        assert want == got
