#!/usr/bin/env python

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        head = nums[0]
        tail = nums[1:]
        without_head = self.subsets(tail)
        with_head = [[head] + l for l in without_head]
        return with_head + without_head


if __name__ == "__main__":
    print("hi")
    A = [1, 2, 3]
    want = [
        [3],
        [1],
        [2],
        [1, 2, 3],
        [1, 3],
        [2, 3],
        [1, 2],
        [],
    ]

    S = Solution()
    got = S.subsets(A)
    print(f"Match? {want == got}\nWant {want}\nGot {got}")
    assert want == got
