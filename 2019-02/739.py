#!/usr/bin/env python

# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature. If there is no future day for which this is possible, put 0
# instead.

# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

# Note: The length of temperatures will be in the range [1, 30000]. Each
# temperature will be an integer in the range [30, 100].


from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        i = len(T) - 2
        while i >= 0:
            j = i + 1
            while j < len(T):
                if T[j] > T[i]:
                    result[i] = j - i
                    break
                if result[j] == 0:
                    break
                j += result[j]
            i -= 1
        return result


if __name__ == "__main__":
    print("Hello")
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    want = [1, 1, 4, 2, 1, 1, 0, 0]
    S = Solution()
    got = S.dailyTemperatures(T)
    print(f"Match? {want == got} got {got} want {want}")
    assert want == got
