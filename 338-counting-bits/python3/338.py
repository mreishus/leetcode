#!/usr/bin/python3
from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        r = [0] * (num+1)
        for i in range(len(r)):
            if i == 0:
                r[i] = 0
            else:
                r[i] = r[i & (i-1)] + 1
        return r

expected_result = [0,1,1,2,1,2]
s = Solution()
#actual_result = s.countBits(500_000) # 0.134s fast version, 0.816s slow version
actual_result = s.countBits(5)
print("Expect to see")
print(expected_result)
print("Actual Result")
print(actual_result)
print("Are same?")
print(actual_result == expected_result)
