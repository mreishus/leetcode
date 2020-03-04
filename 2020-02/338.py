#!/usr/bin/env python3
from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        return self.countBitsFast2(num)
        # return self.countBitsFast(num)
        # return self.countBitsSlow(num)

    # DP: Number of bits in binary I is equal to
    # that number of bits in right shifted version of I, plus
    # 1 if odd, 0 if even
    def countBitsFast(self, num: int) -> List[int]:
        bs = [0 for _ in range(num+1)]
        for i in range(1, num+1):
            bs[i] = bs[i // 2] + (i % 2)
        return bs

    # DP:  Setting "i & (i-1)" turns off the rightmost
    # bit of a binary number. (Kernighan)
    def countBitsFast2(self, num: int) -> List[int]:
        bs = [0 for _ in range(num+1)]
        for i in range(1, num+1):
            bs[i] = bs[i & (i-1)] + 1
        return bs

    def countBitsSlow(self, num: int) -> List[int]:
        return [self.bits(i) for i in range(num+1)]

    def bits(self, num: int) -> int:
        b = 0
        while num > 0:
            if num % 2 == 1:
                b += 1
            num = num // 2
        return b

s = Solution()
got = s.countBits(5)
want = [0,1,1,2,1,2]
print(f"got: {got} want: {want} same: {got == want}")
