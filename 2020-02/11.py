#!/usr/bin/env python

# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
# forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

from typing import List


class Solution:
    def maxAreaSlow(self, height: List[int]) -> int:
        """ This way is too slow. N^2 """
        answer = 0
        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height[i + 1 :], i + 1):
                width = j - i
                h = min(h1, h2)
                area = width * h
                answer = max(answer, area)
                # print(f"{i} {j} | {h1} {h2} | {width} {h} | {area}")

        return answer

    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        answer = 0
        while i < j:
            width = j - i
            h = min(height[i], height[j])
            area = width * h
            answer = max(answer, area)

            if height[i] < height[j]:
                i += 1
            else:  # height[i] >= height[j]
                j -= 1
        return answer


if __name__ == "__main__":
    print("Expect: 49")
    got = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(got)
