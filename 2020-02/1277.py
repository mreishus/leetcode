#!/usr/bin/env python
"""
Given a m * n matrix of ones and zeros, return how many square submatrices have
all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.

Constraints:

    1 <= arr.length <= 300
    1 <= arr[0].length <= 300
    0 <= arr[i][j] <= 1
"""

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        result = 0

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    continue
                if y == 0 or x == 0:
                    result += 1
                else:
                    val = 1 + min(
                        matrix[y - 1][x], matrix[y][x - 1], matrix[y - 1][x - 1]
                    )
                    result += val
                    matrix[y][x] = val
        return result
