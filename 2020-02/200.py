#!/usr/bin/env python

"""
200. Number of Islands Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        len_y = len(grid)
        if len_y == 0:
            return 0
        len_x = len(grid[0])

        def valid(x, y):
            return 0 <= x < len_x and 0 <= y < len_y

        def neighbors(x, y):
            n = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            return [(x, y) for (x, y) in n if valid(x, y)]

        def bfs_mark_island(x, y):
            q = [(x, y)]
            while len(q) > 0:
                (x, y) = q.pop(0)
                if (x, y) in discovered_land or grid[y][x] == "0":
                    continue
                discovered_land.add((x, y))

                for (nx, ny) in neighbors(x, y):
                    if (nx, ny) not in discovered_land:
                        q.append((nx, ny))

        island_count = 0
        discovered_land = set()

        # Not completely happy with this:
        # This outer walkthrough of all items seems slower than needed.
        for y in range(len_y):
            for x in range(len_x):
                if grid[y][x] == "1" and (x, y) not in discovered_land:
                    island_count += 1
                    bfs_mark_island(x, y)
        return island_count


if __name__ == "__main__":
    print("200. Number of Islands")
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print("Expect: 1")
    print(Solution().numIslands(grid))

    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "0", "1", "1"],
    ]
    print("Expect: 2")
    print(Solution().numIslands(grid))
