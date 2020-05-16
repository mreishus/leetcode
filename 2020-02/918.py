#!/usr/bin/env python

from typing import List

"""
Given a circular array C of integers represented by A, find the maximum
possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of
the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] =
C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most
once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist
i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1

"""


# Here is a clever algorithm.
# Finds both max and min subarray sum and standard total.

# If max sum < 0:
# All numbers are negative.  Return max sum.
# Otherwise:
# Return max of (max_sum, total-min_sum).
# Case 1:  [min--| ------max------ | --min]
# Case 2:  [max--| ------min------ | --max]
#   ^ Here, the value is total - min
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        min_sum = float("+inf")
        max_ending_here = float("-inf")
        min_ending_here = float("+inf")
        total = 0
        for num in nums:
            max_ending_here = max(num, num + max_ending_here)
            max_sum = max(max_sum, max_ending_here)

            min_ending_here = min(num, num + min_ending_here)
            min_sum = min(min_sum, min_ending_here)

            total += num
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)


if __name__ == "__main__":
    cases = [
        ([1, -2, 3, -2], 3),
        ([5, -3, 5], 10),
        ([3, -1, 2, -1], 4),
        ([3, -2, 2, -3], 3),
        ([-2, -3, -1], -1),
        ([-2, -3, -1], -1),
    ]
    for (nums, want) in cases:
        got = Solution().maxSubarraySumCircular(nums)
        print(f"Pass? {got == want} | got {got} want {want} | nums {nums}")
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    answer = Solution().maxSubarraySumCircular(A)
    print("Expect: 6")
    print(answer)
