#!/usr/bin/env python

from math import factorial

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).

# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).

# How many possible unique paths are there?


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m = m - 1
        n = n - 1
        a = factorial(m + n) / (factorial(m) * factorial(n))
        return int(a)


if __name__ == "__main__":
    print("Expect: 3")
    print(Solution().uniquePaths(3, 2))
    print("Expect: 28")
    print(Solution().uniquePaths(7, 3))
