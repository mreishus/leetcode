#!/usr/bin/env python
"""
451. Sort Characters By Frequency
Medium

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""


from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        return "".join([letter * freq for (letter, freq) in counts.most_common()])


if __name__ == "__main__":
    # cases = [("tree", "eert")]
    cases = [("tree", "eetr")]  # Also valid
    for (s, want) in cases:
        got = Solution().frequencySort(s)
        print(f"Pass? {want == got} | Got {got} Want {want} | s {s}")
        assert want == got
