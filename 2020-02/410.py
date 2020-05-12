#!/usr/bin/env python

"""
410. Split Array Largest Sum
Hard

Given an array which consists of non-negative integers and an integer m, you
can split the array into m non-empty continuous subarrays. Write an algorithm
to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

    1 ≤ n ≤ 1000
    1 ≤ m ≤ min(50, n)

Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

"""


from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def isPossible(target: int) -> bool:
            cuts = m - 1
            # print(f"-- Is poss? Target {target} Cuts {cuts} m {m}")
            if cuts == 0:
                return sum(nums) <= target
            total = 0
            for num in nums:
                if num > target:
                    return False
                if total + num > target:
                    cuts -= 1
                    if cuts < 0:
                        return False
                    total = 0
                    total += num
                else:
                    total += num
                # print(f"num {num} | total {total} | cuts {cuts}")

            if total <= target:
                return True
            return cuts > 0

        low = 0
        high = sum(nums)
        answer = 0
        while low <= high:
            mid = (low + high) // 2
            possible = isPossible(mid)
            # print(f"mid {mid} possible {possible}")
            if possible:
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    print("410 Split Array Largest Sum")
    cases = [
        ([7, 2, 5, 10, 8], 2, 18),
        ([1, 2147483647], 2, 2147483647),
        ([2, 3, 1, 2, 4, 3], 5, 4),
    ]
    # nums = [7, 2, 5, 10, 8]
    # m = 2
    # want = 18
    for (nums, m, want) in cases:
        got = Solution().splitArray(nums, m)
        print(f"Pass? {want == got} | got {got} | want {want}")
        assert want == got
