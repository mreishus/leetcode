#!/usr/bin/env python
"""
We write the integers of A and B (in the order they are given) on two separate
horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i]
and B[j] such that:

    A[i] == B[j];
    The line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting lines cannot intersect even at the endpoints: each
number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

(This is also longest common subsequence, kinda like levenstein distance but not)
"""


from typing import List
from functools import lru_cache


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        @lru_cache(None)
        def helper(i, j):
            if i < 0 or j < 0:
                return 0
            if A[i] == B[j]:
                return 1 + helper(i - 1, j - 1)
            return max(helper(i - 1, j), helper(i, j - 1))

        return helper(len(A) - 1, len(B) - 1)


if __name__ == "__main__":
    cases = [
        ([1, 4, 2], [1, 2, 4], 2),
        ([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2], 3),
        ([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1], 2),
    ]
    for (A, B, want) in cases:
        got = Solution().maxUncrossedLines(A, B)
        print(f"Pass? {got == want} | got {got} | want {want} | {A} {B}")
