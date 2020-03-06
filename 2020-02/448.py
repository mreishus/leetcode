#!/usr/bin/env python


from typing import List


# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.

# Example:

# Input: [4,3,2,7,8,2,3,1]

# Output: [5,6]


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, _ in enumerate(nums):
            real_pos = abs(nums[i]) - 1
            if nums[real_pos] > 0:
                nums[real_pos] *= -1
        return [i + 1 for (i, e) in enumerate(nums) if e > 0]


if __name__ == "__main__":
    print("hi")
    A = [4, 3, 2, 7, 8, 2, 3, 1]
    want = [5, 6]
    S = Solution()
    got = S.findDisappearedNumbers(A)
    print(f"Match? {want == got}\ngot {got} want {want}")
    assert want == got
