#!/usr/bin/env python
"""
Given two strings S and T, return if they are equal when both are typed into
empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

Follow up:

    Can you solve it in O(N) time and O(1) space?
"""

from typing import List


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.process(S) == self.process(T)

    def process(self, S: str) -> List[str]:
        S = list(S)
        s_writer = 0
        for s_reader, letter in enumerate(S):
            if letter == "#":
                s_writer = max(0, s_writer - 1)

            # print(f"{s_reader} {letter} {s_writer}")
            S[s_writer] = S[s_reader]
            if letter != "#":
                s_writer += 1

        return S[0:s_writer]


if __name__ == "__main__":
    print("Backspace string compare")
    cases = [
        ("ab#c", "ad#c", True),
        ("ab##", "c#d#", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
    ]
    for (s1, s2, want) in cases:
        got = Solution().backspaceCompare(s1, s2)
        print(f"Pass? {got == want} | Got {got} | Want {want} | Inputs {s1} {s2}")
