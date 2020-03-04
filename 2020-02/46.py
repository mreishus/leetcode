#!/usr/bin/env python

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        answers = []
        for i, elem in enumerate(nums):
            without = nums[:i] + nums[i + 1 :]
            subperms = self.permute(without)
            for p in subperms:
                answers.append([elem] + p)
        return answers


if __name__ == "__main__":
    print("hi")
    s = Solution()
    print(s.permute([1, 2, 3]))
