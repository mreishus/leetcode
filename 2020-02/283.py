#!/usr/bin/env python

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        writer = 0
        for reader, elem in enumerate(nums):
            if elem == 0:
                pass
            else:
                nums[writer] = elem
                writer += 1

        while writer < len(nums):
            nums[writer] = 0
            writer += 1


if __name__ == "__main__":
    print("hi")
    A = [0, 1, 0, 3, 12]
    want = [1, 3, 12, 0, 0]

    S = Solution()
    S.moveZeroes(A)
    got = A
    print(f"Match? {want == got} Want {want} Got {got}")
    assert want == got
