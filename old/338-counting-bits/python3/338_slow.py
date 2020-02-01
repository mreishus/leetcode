#!/usr/bin/python3
from typing import List

class Solution:
    def countBinaryOnes(self, x):
        count = 0
        while x > 0:
            if (x % 2 == 1):
                count += 1
            x = x >> 1
        return count
    def countBits(self, num: int) -> List[int]:
        r = list(range(num+1))
        return list(map(self.countBinaryOnes, r))

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
