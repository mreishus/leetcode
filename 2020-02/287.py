#!/usr/bin/env python

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        print("Begin")
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        find = 0
        while True:
            find = nums[find]
            slow = nums[slow]
            if find == slow:
                return find


if __name__ == "__main__":
    A = [1, 3, 4, 2, 2]
    print(Solution().findDuplicate(A))
