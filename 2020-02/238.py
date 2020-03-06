#!/usr/bin/env python

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1] * len(nums)
        backward = [1] * len(nums)
        for i in range(1, len(nums)):
            forward[i] = forward[i - 1] * nums[i - 1]
        for i in reversed(range(len(nums) - 1)):
            backward[i] = backward[i + 1] * nums[i + 1]

        return [forward[i] * backward[i] for (i, _) in enumerate(nums)]


if __name__ == "__main__":
    print("hi")
    A = [1, 2, 3, 4]
    want = [24, 12, 8, 6]

    S = Solution()
    got = S.productExceptSelf(A)
    print(f"Match? {want == got} Want {want} Got {got}")
    assert want == got
