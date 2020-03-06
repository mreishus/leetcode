#!/usr/bin/env python


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = None
        count = 0
        for num in nums:
            if num != cand and count == 0:
                cand = num
            elif num != cand:
                count -= 1
            else:
                count += 1

        return cand


if __name__ == "__main__":
    print("hi")
    A = [2, 2, 1, 1, 1, 2, 2]
    want = 2
    S = Solution()
    got = S.majorityElement(A)
    print(f"Match? {want == got}\ngot {got} want {want}")
    assert want == got
