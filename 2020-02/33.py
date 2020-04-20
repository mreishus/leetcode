#!/usr/bin/python
"""
Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0 Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3 Output: -1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:
                # low - mid is sorted
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:  # mid - high is sorted
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


if __name__ == "__main__":
    print("33 - Search in rotated sorted array")
    s = Solution()
    cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([3, 5, 1], 3, -0),
        ([3, 1], 1, 1),
        ([5, 1, 3], 5, 0),
        ([4, 5, 6, 7, 8, 1, 2, 3], 8, 4),
        ([5, 1, 3], 3, 2),
    ]
    for (nums, target, want) in cases:
        got = s.search(nums, target)
        print(
            f"Pass? {got == want} | nums {nums} | target {target} | got {got} | want {want}"
        )
