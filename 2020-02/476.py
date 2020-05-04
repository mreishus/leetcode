#!/usr/bin/env python
"""
476. Number Complement
Easy

Given a positive integer, output its complement number. The complement strategy
is to flip the bits of its binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and
its complement is 010. So you need to output 2.

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and
its complement is 0. So you need to output 0.

Note:

    The given integer is guaranteed to fit within the range of a 32-bit signed
    integer.  You could assume no leading zero bit in the integer’s binary
    representation.  This question is the same as 1009:
    https://leetcode.com/problems/complement-of-base-10-integer/


"""


class Solution:
    def findComplement(self, num: int) -> int:
        # Find size of number
        size = 32
        while num < (1 << size):
            size -= 1
        size += 1

        # Flip each bit individually
        # for i in range(size):
        #     num = num ^ (1 << i)

        # Flip them all at once
        num = num ^ ((1 << size) - 1)

        return num


if __name__ == "__main__":
    cases = [(5, 2), (1, 0)]
    for (num, want) in cases:
        got = Solution().findComplement(num)
        print(f"Pass? {want == got} | got {got} | want {want} | num {num}")
