#!/usr/bin/env python3
from typing import List

class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # Init Answers array
        answers = []
        for i in range(len(temps)):
            answers.append(0)

        # Work backwards through the temps array.
        # Skip the last entry, because it is always 0.
        for i in reversed(range(len(temps) - 1)):
            # Go to the right, looking for a higher number,
            # but reuse the information we've already stored
            # in the answers array.
            j = i+1
            while (j < len(temps)):
                if temps[j] > temps[i]:
                    answers[i] = j - i
                    break
                if answers[j] == 0:
                    break
                j += answers[j]
        return answers

s = Solution()
actual_result = s.dailyTemperatures([55,38,53,81,61,93,97,32,43,78]);
expected_result =                   [3, 1, 1, 2, 1, 1, 0, 1, 1,  0];
print("Expected Result", expected_result)
print("Actual Result  ", actual_result)
print("Same?")
print(actual_result == expected_result)
