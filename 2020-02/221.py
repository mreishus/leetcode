#!/usr/bin/env python
"""
221. Maximal Square Medium

Given a 2D binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""


from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Calculate Array dimensions
        ylen = len(matrix)
        if ylen == 0:
            return 0
        xlen = len(matrix[0])

        # Create new blank array with same size as matrix
        dp = []
        for y in range(ylen):
            dp.append([0] * xlen)

        # Safe way of getting value from DP - returns 0 if out of bounds
        def mget(grid, y, x):
            if y < 0 or x < 0 or y >= ylen or x >= xlen:
                return 0
            return grid[y][x]

        max_val = 0
        for y in range(ylen):
            for x in range(xlen):
                if matrix[y][x] == 1 or matrix[y][x] == "1":
                    dp[y][x] = (
                        min(
                            [
                                mget(dp, y - 1, x),
                                mget(dp, y, x - 1),
                                mget(dp, y - 1, x - 1),
                            ]
                        )
                        + 1
                    )
                    max_val = max(max_val, dp[y][x])

        # print("Matrix:")
        # for y in range(ylen):
        #     for x in range(xlen):
        #         print(matrix[y][x], end=" ")
        #     print("")

        # print(" ")
        # print("DP:")
        # for y in range(ylen):
        #     for x in range(xlen):
        #         print(dp[y][x], end=" ")
        #     print("")

        return max_val * max_val


if __name__ == "__main__":
    print("212")
    A = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
    got = Solution().maximalSquare(A)
    want = 4
    print(f"Pass? {got == want} | Got {got} | want {want} | A {A}")

    A = [[0]]
    got = Solution().maximalSquare(A)
    want = 0
    print(f"Pass? {got == want} | Got {got} | want {want} | A {A}")
