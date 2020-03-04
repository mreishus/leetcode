#!/usr/bin/env python


from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = Counter(nums)
        s = [(-count, num) for (num, count) in seen.items()]
        heapq.heapify(s)

        result = []
        for _ in range(k):
            (negcount, num) = heapq.heappop(s)
            result.append(num)
        return result


if __name__ == "__main__":
    print("hi")
    S = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(S.topKFrequent(nums, k))
