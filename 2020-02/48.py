#!/usr/bin/env python


from typing import List

# 1 2 3
# 4 5 6
# 7 8 9

# 7 4 1
# 8 5 2
# 9 6 3


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Transpose (Flip around diagonal)
        l = len(matrix)
        for i in range(l):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Flip horizontal
        for i in range(l):
            for j in range(l // 2):
                k = l - j - 1
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]


if __name__ == "__main__":
    print("hi")
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    want = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    S = Solution()
    S.rotate(A)
    got = A
    print(f"Match? {want == got}\ngot {got} want {want}")
    assert want == got
