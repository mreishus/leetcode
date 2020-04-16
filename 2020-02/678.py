#!/usr/bin/env python

import functools


class Solution:
    def checkValidString(self, s: str) -> bool:
        @functools.lru_cache
        def helper(a, level) -> bool:
            for i in range(a, len(s)):
                char = s[i]
                if char == "(":
                    level += 1
                elif char == ")":
                    level -= 1
                    if level < 0:
                        return False
                elif char == "*":
                    return any(
                        [
                            helper(i + 1, level - 1),
                            helper(i + 1, level),
                            helper(i + 1, level + 1),
                        ]
                    )
            return level == 0

        return helper(0, 0)


if __name__ == "__main__":
    valids = ["()", "(*)", "(*))", "(()())"]
    invalids = ["((", ")(", "())", "(()()))"]
    for s in valids:
        got = Solution().checkValidString(s)
        want = True
        print(f"Testing {s}.. ", end="")
        assert got == want
        print("Passed.")
    for s in invalids:
        got = Solution().checkValidString(s)
        want = False
        print(f"Testing {s}.. ", end="")
        assert got == want
        print("Passed.")
