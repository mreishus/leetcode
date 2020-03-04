#!/usr/bin/python

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(s, max_open: int, level: int):
            if max_open == 0 and level == 0:
                return [s]

            answers = []
            if max_open > 0:
                answers += helper(s + "(", max_open - 1, level + 1)
            if level > 0:
                answers += helper(s + ")", max_open, level - 1)
            return answers

        return helper("", n, 0)


if __name__ == "__main__":
    print("hi")
    s = Solution()
    a = s.generateParenthesis(3)
    print(a)
