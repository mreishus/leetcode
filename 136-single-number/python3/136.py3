#!/usr/bin/env python3
from typing import List
import functools

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce(lambda acc, x: x ^ acc, nums)

print("Expected Answer: 4")
s = Solution()
answer = s.singleNumber([4, 1, 2, 1, 2])
print("Actual Answer: " + str(answer))
