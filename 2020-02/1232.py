#!/usr/bin/env python
"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
represents the coordinate of a point. Check if these points make a straight
line in the XY plane.
"""


from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 2:
            return False
        if len(coordinates) == 2:
            return True

        [x1, y1] = coordinates[0]
        [x2, y2] = coordinates[1]

        rise = y2 - y1
        run = x2 - x1
        if run == 0:
            return False
        m = rise / run

        # y = mx + b
        # y - mx = b
        b = y1 - m * x1

        for [x3, y3] in coordinates[2:]:
            test_y = m * x3 + b
            if test_y != y3:
                return False

        return True


if __name__ == "__main__":
    cases = [
        ([[0, 0], [3, 2], [6, 4]], True),
        ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], True),
        ([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]], False),
    ]
    for (coords, want) in cases:
        got = Solution().checkStraightLine(coords)
        assert got == want
