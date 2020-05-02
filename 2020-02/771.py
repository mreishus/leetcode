#!/usr/bin/env python
"""
You're given strings J representing the types of stones that are jewels, and S
representing the stones you have.  Each character in S is a type of stone you
have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are
letters. Letters are case sensitive, so "a" is considered a different type of
stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0

Note:

    S and J will consist of letters and have length at most 50.
    The characters in J are distinct.
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        return sum(1 for s in S if s in jewels)


if __name__ == "__main__":
    cases = [
        ("aA", "aAAbbbb", 3),
        ("z", "ZZ", 0),
    ]
    for (J, S, want) in cases:
        got = Solution().numJewelsInStones(J, S)
        print(f"Pass? {want == got} | got {got} | want {want} | J {J} | S {S}")
