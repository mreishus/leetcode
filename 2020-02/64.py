#!/usr/bin/env python

from typing import List

import heapq
from collections import defaultdict


class Solution:
    def neighbors(self, x1, y1, xe, ye):
        if x1 + 1 <= xe:
            yield (x1 + 1, y1)
        if y1 + 1 <= ye:
            yield (x1, y1 + 1)

    def minPathSum(self, grid: List[List[int]]) -> int:
        x0, y0 = 0, 0
        ye, xe = len(grid) - 1, len(grid[0]) - 1
        # print(f"xe {xe} ye {ye}")
        seen = set()
        dist_to = defaultdict(lambda: 999_999_999)
        dist_to[(x0, y0)] = grid[y0][x0]
        edge_to = {}
        q = [(grid[y0][x0], x0, y0)]
        heapq.heapify(q)
        while len(q) > 0:
            cost, x1, y1 = heapq.heappop(q)
            if (x1, y1) in seen:
                continue
            seen.add((x1, y1))
            for (x2, y2) in self.neighbors(x1, y1, xe, ye):
                cost_there = cost + grid[y2][x2]
                if cost_there < dist_to[(x2, y2)]:
                    dist_to[(x2, y2)] = cost_there
                    edge_to[(x2, y2)] = (x1, y1)
                    heapq.heappush(q, (cost_there, x2, y2))
        if dist_to[(xe, ye)] == 999_999_999:
            return 0
        print(grid)
        print(dist_to)
        return dist_to[(xe, ye)]


if __name__ == "__main__":
    # print("64")
    # grid = [
    #     [1, 3, 1],
    #     [1, 5, 1],
    #     [4, 2, 1],
    # ]
    # print("Expect: 7")
    # print(Solution().minPathSum(grid))
    grid2 = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    print("Expect: 12")
    print(Solution().minPathSum(grid2))
