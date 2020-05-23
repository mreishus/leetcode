#!/usr/bin/env python
"""
986. Interval List Intersections Medium

Given two lists of closed intervals, each list of intervals is pairwise
disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real
numbers x with a <= x <= b.  The intersection of two closed intervals is a set
of real numbers that is either empty, or can be represented as a closed
interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

"""

from typing import List
from collections import namedtuple

Endpoint = namedtuple("Endpoint", ("time", "is_end"))


class Solution:
    def intervalIntersection(
        self, A: List[List[int]], B: List[List[int]]
    ) -> List[List[int]]:
        endpoints = []
        for l in [A, B]:
            for [start, end] in l:
                endpoints.append(Endpoint(start, False))
                endpoints.append(Endpoint(end, True))
        endpoints.sort()

        meetings = 0
        result = []
        begin_overlap_time = None
        end_overlap_time = None
        for endpoint in endpoints:
            if endpoint.is_end:
                meetings -= 1
                if meetings == 1:
                    end_overlap_time = endpoint.time
                    result.append([begin_overlap_time, end_overlap_time])
            else:
                meetings += 1
                if meetings == 2:
                    begin_overlap_time = endpoint.time
        return result


if __name__ == "__main__":
    print("986 interval list intersection")
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    want = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    got = Solution().intervalIntersection(A, B)
    print(f"Pass? {want == got} | Got {got} Want {want}")
    assert want == got
