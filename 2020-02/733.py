#!/usr/bin/env python

"""
733 Flood Fill - Easy

An image is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of
the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

Note:
The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""


from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        max_y = len(image) - 1
        if max_y == 0:
            return image
        max_x = len(image[0]) - 1

        start_color = image[sr][sc]

        def neighbors(xp, yp):
            candidates = [
                (xp + 1, yp),
                (xp - 1, yp),
                (xp, yp + 1),
                (xp, yp - 1),
            ]
            for (x, y) in candidates:
                if 0 <= x <= max_x and 0 <= y <= max_y and image[y][x] == start_color:
                    yield (x, y)

        q = [(sc, sr)]
        seen = set()
        while len(q) > 0:
            x, y = q.pop(0)
            seen.add((x, y))
            for x2, y2 in neighbors(x, y):
                if (x2, y2) not in seen:
                    q.append((x2, y2))
            image[y][x] = newColor
        return image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    want = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    got = Solution().floodFill(image, 1, 1, 2)
    print(f"Pass? {want == got}")
    print("Want:")
    print(want)
    print("Got:")
    print(got)

    image = [[0, 0, 0], [1, 0, 0]]
    want = [[0, 0, 0], [2, 0, 0]]
    got = Solution().floodFill(image, 1, 0, 2)
    print(f"Pass? {want == got}")
    print("Want:")
    print(want)
    print("Got:")
    print(got)
