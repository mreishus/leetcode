#!/usr/bin/env python

from typing import List
from functools import reduce
from operator import xor

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)

s = Solution()
got = s.singleNumber([2, 2, 1])
want = 1
print(f"got {got} want {want} pass {got == want}")
got = s.singleNumber([4, 1, 2, 1, 2])
want = 4
print(f"got {got} want {want} pass {got == want}")
