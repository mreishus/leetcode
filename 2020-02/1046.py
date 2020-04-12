#!/usr/bin/env python

"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose
the stones have weights x and y with x <= y.  The result of this smash is:

    If x == y, both stones are totally destroyed;
    If x != y, the stone of weight x is totally destroyed, and the stone of
    weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or
0 if there are no stones left.)


Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

Note:

    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
"""

from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        istones = [x * -1 for x in stones]
        heapq.heapify(istones)
        while len(istones) >= 2:
            s1 = heapq.heappop(istones)
            s2 = heapq.heappop(istones)
            if s1 != s2:
                s3 = s2 - s1
                heapq.heappush(istones, s3 * -1)
        if len(istones) == 0:
            return 0
        return istones[0] * -1


if __name__ == "__main__":
    print("Last Stone Weight")
    print("Expect: 1:")
    print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
