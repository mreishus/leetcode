#!/usr/bin/python
"""
Leftmost Column with at Least a One

(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of
the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column
index(0-indexed) with at least a 1 in it. If such index doesn't exist, return
-1.

You can't access the Binary Matrix directly.  You may only access the matrix
using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y)
(0-indexed).  BinaryMatrix.dimensions() returns a list of 2 elements [n, m],
which means the matrix is n * m.

Submissions making more than 1000 calls to BinaryMatrix.get will be judged
Wrong Answer.  Also, any solutions that attempt to circumvent the judge will
result in disqualification.
"""

from typing import List


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# (I had to implement it anyway -Matt)
# """
class BinaryMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def get(self, x: int, y: int) -> int:
        # return self.matrix[y][x]
        return self.matrix[x][y]

    def dimensions(self) -> List[int]:
        x = len(self.matrix[0])
        y = len(self.matrix)
        return [y, x]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        def bin_search(this_y, max_x):
            """ Bin search horizontally across:
            Row: this_y
            X: 0 to max_x (inclusive)
            Look for the first 1.
            """
            low = 0
            high = max_x
            result = None
            while low <= high:
                mid = (low + high) // 2
                val = binaryMatrix.get(this_y, mid)
                # print(f"  get({mid}, {this_y}) = {val}")
                if val == 1:
                    if result is None or mid < result:
                        result = mid
                    high = mid - 1
                else:  # val == 0
                    low = mid + 1
                # print(f"  low {low} high {high} mid {mid} result {result} val {val}")
            return result

        outer_result = -1
        xlen, ylen = binaryMatrix.dimensions()
        xlen, ylen = ylen, xlen
        # print(f"=== xlen {xlen} ylen {ylen}")
        for y in range(ylen):

            # print(f"+ search {y} {xlen -1}")
            right_x = xlen - 1
            if outer_result != -1 and outer_result < right_x:
                right_x = outer_result
            this_result = bin_search(y, right_x)

            if this_result is not None:
                if outer_result == -1:
                    outer_result = this_result
                else:
                    outer_result = min(outer_result, this_result)
        return outer_result


if __name__ == "__main__":
    m = BinaryMatrix([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]])
    xlen, ylen = m.dimensions()
    for y in range(ylen):
        for x in range(xlen):
            print(m.get(x, y), end=" ")
        print("")
    print("---")
    print("Expect: 1")
    m = BinaryMatrix([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]])
    print(Solution().leftMostColumnWithOne(m))
    print("Expect: 0")
    m = BinaryMatrix([[0, 0], [1, 1]])
    print(Solution().leftMostColumnWithOne(m))
