#!/usr/bin/env python


import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)
        for num in nums[k:]:
            heapq.heappush(h, num)
            if len(h) > k:
                heapq.heappop(h)
        return heapq.heappop(h)


if __name__ == "__main__":
    print("HI")
    A = [3, 2, 1, 5, 6, 4]
    print("Expect: 5")
    print(Solution().findKthLargest(A, 2))
    A = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    print("Expect: 4")
    print(Solution().findKthLargest(A, 4))
