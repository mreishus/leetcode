#!/usr/bin/env python
"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.
"""

from typing import List


class Solution:
    """ Solution """

    def isHappy(self, n: int) -> bool:
        """ Is n a happy number? See above for definition. """
        seen = set()

        while True:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = sum(z * z for z in self.digits(n))

    def digits(self, n: int) -> List[int]:
        """ Digits(4231) = [1, 2, 3, 4] """
        answer = []
        while n > 0:
            digit = n % 10
            answer.append(digit)
            n //= 10
        return answer


if __name__ == "__main__":
    print("expect true")
    print(Solution().isHappy(19))
